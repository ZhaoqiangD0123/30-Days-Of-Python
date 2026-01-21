import pymongo
import certifi

# 1. 连接 (老规矩)
connection_string = "mongodb+srv://zhaoqiangding008:Dzq963852741.@cluster0.auxnflt.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db = client['research_lab']
col = db['hacker_news']

# 2. 查询所有数据
# find() 不填参数就是查所有
# 注意：find() 返回的不是列表，是一个“游标 (Cursor)”。
# 游标就像是一个指针，你得遍历它，或者把它强转成 list 才能看到数据。
cursor = col.find().limit(5)  # limit(5) 表示只取前5条，防止数据太多刷屏

print("--- 前5条新闻 ---")
for doc in cursor:
    print(doc)
    # 你会发现打印出来的是字典，包含了 _id, title, url 等字段


print("\n--- 筛选评论数 > 500 的热门新闻 ---")

# 语法：{ '字段名': { '$操作符': 值 } }
# $gt 意思是 greater than (大于)
# $lt 意思是 less than (小于)
# $gte (大于等于), $lte (小于等于)
query = { 'num_comments': { '$gt': 500 } }

cursor = col.find(query)

for doc in cursor:
    # 打印标题和评论数
    print(f"[{doc['num_comments']}评] {doc['title']}")
import pandas as pd

print("\n--- 将查询结果转回 DataFrame ---")

# 1. 查出所有 Python 相关新闻
cursor = col.find({ 'title': { '$regex': 'Python', '$options': 'i' } })

# 2. 直接把游标转换成列表，再喂给 DataFrame
# list(cursor) 会把游标里的数据全部拉取到内存里
df_python = pd.DataFrame(list(cursor))

# 3. 现在的 df_python 就是你熟悉的表格了！
print(df_python.head())
print(f"数据形状: {df_python.shape}")