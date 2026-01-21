from flask import Flask, render_template
import pandas as pd
import os  # 引入操作系统模块，专门处理路径

app = Flask(__name__)


# --- 1. 定义首页 (防止打开网页 404) ---
@app.route('/')
def home():
    return '''
    <h1>网站已启动! 🚀</h1>
    <a href="/analysis">点击这里查看数据分析报告</a>
    '''


# --- 2. 定义分析页 ---
@app.route('/analysis')
def show_data():
    try:
        # 【关键修改】：获取当前 app.py 文件所在的绝对路径
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接出 csv 的完整路径
        csv_path = os.path.join(base_dir, 'hacker_news.csv')

        # 读取
        df = pd.read_csv(csv_path)

        # 数据处理
        rows = df.shape[0]
        columns = df.columns.tolist()

        # 转换前10行数据为HTML
        table_html = df.head(10).to_html(classes='data-table', header="true", index=False)

        return render_template('analysis.html',
                               row_count=rows,
                               cols=columns,
                               table=table_html)
    except Exception as e:
        # 如果出错，把错误打印在网页上方便调试
        return f"<h1>读取出错啦 😭</h1><p>{e}</p>"


if __name__ == '__main__':
    app.run(debug=True, port=5000)