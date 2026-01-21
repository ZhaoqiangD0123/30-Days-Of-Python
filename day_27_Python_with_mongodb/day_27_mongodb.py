import pymongo
import certifi # 刚才修好的SSL证书库

# 1. 连接 (复用你刚才成功的代码)
# ⚠️ 替换为你自己的连接字符串
connection_string = "mongodb+srv://zhaoqiangding008:Dzq963852741.@cluster0.auxnflt.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())

# 2. 选库、选表 (就像选 Excel 文件和 Sheet)
# 只要你写了这个名字，MongoDB 就会自动创建它，不需要手动建
db = client['research_lab']      # 数据库名：research_lab
col = db['students']             # 集合(表)名：students

# 3. 准备一条数据 (字典格式)
student_1 = {
    'name': 'JinTian',
    'id': 2026002,
    'role': 'Researcher',
    'skills': ['Python', 'MongoDB', 'Data Mining'],
    'score': 99.5
}

# 4. 写入数据 (Action!)
try:
    result = col.insert_one(student_1)
    print(f"✅ 目标一达成！数据写入成功。")
    print(f"这条数据的身份证号 (_id) 是: {result.inserted_id}")
except Exception as e:
    print(f"❌ 写入失败: {e}")