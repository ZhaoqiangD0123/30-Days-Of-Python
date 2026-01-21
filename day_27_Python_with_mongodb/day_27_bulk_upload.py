import pymongo
import certifi
import pandas as pd
import os

# 1. 连接云端 (还是原来的配方)
connection_string = "mongodb+srv://zhaoqiangding008:Dzq963852741.@cluster0.auxnflt.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())

# 2. 选库、选表
# 我们把新闻数据放在 research_lab 库下的 hacker_news 表里
db = client['research_lab']
col = db['hacker_news']

# 3. 读取 CSV 文件
# 使用绝对路径是个好习惯，防止 Python 找不到文件
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'hacker_news.csv')

print(f"正在读取文件: {csv_path}")

try:
    # Pandas 读取 csv
    df = pd.read_csv(csv_path)

    # 【关键步骤】数据清洗与转换
    # MongoDB 不喜欢 CSV 里的 NaN (空值)，我们先把空值填上
    df = df.fillna('')

    # 将 DataFrame 转为 字典列表 (List of Dictionaries)
    # orient='records' 会把每一行变成一个字典：{'title': '...', 'url': '...'}
    data_list = df.to_dict('records')

    # 4. 批量写入 (Action!)
    if len(data_list) > 0:
        # insert_many 专门用来处理列表，速度极快
        result = col.insert_many(data_list)
        print(f"✅ 成功上传！共写入 {len(result.inserted_ids)} 条新闻。")
    else:
        print("⚠️ CSV 文件是空的，没东西可写。")

except Exception as e:
    print(f"❌ 发生错误: {e}")