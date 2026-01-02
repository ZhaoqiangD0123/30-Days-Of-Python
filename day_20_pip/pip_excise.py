import requests
import json # 引入 json 模块，用于保存源数据

# 1. 获取数据 (使用修正后的 URL)
url = 'https://restcountries.com/v3.1/all?fields=name,population,languages,area,capital'
print("📡 正在连接 API 获取数据...")

try:
    response = requests.get(url)
    response.raise_for_status()
    # 这一步拿到的 countries_data 就是我们的“源数据”
    countries_data = response.json()
    print(type(countries_data))
    print(f"✅ 获取成功！共获取到 {len(countries_data)} 个国家的数据。\n")
except Exception as e:
    print(f"❌ 获取失败: {e}")
    exit()

# ==========================================
# 2. 数据处理 (和之前一样)
# ==========================================

# A. 人口前10
most_populated = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)[:10]

# B. 英语国家
english_countries = []
for country in countries_data:
    if 'eng' in country.get('languages', {}):
        english_countries.append(country['name']['common'])

# C. 面积前10
largest_area = sorted(countries_data, key=lambda x: x.get('area', 0), reverse=True)[:10]

# D. 首都排序 (取前10个演示)
# def get_capital(c):
#     return c.get('capital', [''])[0]
sorted_by_capital = sorted(countries_data, key=lambda x:x.get('capital', ['']))[:10]


# ==========================================
# 3. 核心功能：保存数据到文件
# ==========================================

print("💾 正在保存文件...")

# 🟢 方式一：保存为人类可读的报告 (TXT)
# 我们使用 'w' 模式写入，encoding='utf-8' 非常重要，否则遇到生僻的国家名会报错
with open('countries_report.txt', 'w', encoding='utf-8') as f:
    # 写入标题
    f.write("🌍 世界国家数据分析报告 🌍\n")
    f.write("==============================\n\n")

    # 1. 写入人口数据
    f.write("🏆 人口最多的前 10 个国家:\n")
    for i, country in enumerate(most_populated, 1):
        name = country['name']['common']
        pop = country.get('population', 0)
        # 写入一行，\n 表示换行
        f.write(f"{i}. {name}: {pop:,}\n")
    f.write("\n") # 空一行，好看点

    # 2. 写入面积数据
    f.write("🗺️ 面积最大的前 10 个国家:\n")
    for i, country in enumerate(largest_area, 1):
        name = country['name']['common']
        area = country.get('area', 0)
        f.write(f"{i}. {name}: {area:,.2f} km²\n")
    f.write("\n")

    # 3. 写入英语国家名单
    f.write(f"🗣️ 官方语言包含英语的国家 (共 {len(english_countries)} 个):\n")
    # 使用 join 方法把列表变成一个逗号分隔的长字符串
    f.write(", ".join(english_countries))
    f.write("\n\n")

    f.write("报告生成完毕。")

print("✅ 报告已保存为: countries_report.txt")


# 🟢 方式二：保存原始源数据 (JSON格式的TXT)
# 这样保存下来的文件，下次可以用 json.load() 直接读回来，不用再联网了
with open('source_data.json', 'w', encoding='utf-8') as f:
    # json.dump 是把 Python 列表/字典 直接变成 字符串写入文件
    # ensure_ascii=False 保证能显示中文或特殊字符，而不是乱码
    # indent=4 会让格式自动缩进，很漂亮
    json.dump(countries_data, f, ensure_ascii=False, indent=4)

print("✅ 源数据已备份为: source_data.json")