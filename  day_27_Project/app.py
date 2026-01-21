from flask import Flask, render_template, request
import pymongo
import certifi

app = Flask(__name__)

# --- 1. 连接 MongoDB (这一段你已经很熟了) ---
# ⚠️ 替换成你的真实连接字符串
connection_string = "mongodb+srv://zhaoqiangding008:Dzq963852741.@cluster0.auxnflt.mongodb.net/?appName=Cluster0"
try:
    client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
    db = client['research_lab']
    col = db['hacker_news']
    print("✅ 数据库连接成功！")
except Exception as e:
    print(f"❌ 数据库连接失败: {e}")


# --- 2. 核心路由逻辑 ---
@app.route('/', methods=['GET', 'POST'])
def home():
    news_data = []  # 用来装查到的数据
    keyword = ""  # 用户搜的词
    count = 0  # 查到了多少条

    # 如果用户点击了“搜索”按钮 (POST 请求)
    if request.method == 'POST':
        # 获取用户在输入框里写的字
        keyword = request.form.get('keyword')

        if keyword:
            print(f"🔍 用户正在搜索: {keyword}")

            # 【核心复习】MongoDB 模糊查询
            # $regex: 正则匹配
            # $options: 'i' 忽略大小写
            query = {'title': {'$regex': keyword, '$options': 'i'}}

            # 去数据库查，并只取前 20 条展示
            cursor = col.find(query).limit(20)

            # 转成列表传给网页
            news_data = list(cursor)
            count = len(news_data)

    # 如果是刚打开网页 (GET 请求)，或者搜完了
    # 把数据传给 index.html
    return render_template('index.html', news_list=news_data, keyword=keyword, count=count)


if __name__ == '__main__':
    app.run(debug=True, port=5000)