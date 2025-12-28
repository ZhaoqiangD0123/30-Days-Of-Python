from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Iceland', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 map 将 countries 列表中的每个国家更改为大写，生成一个新列表。
countries_squared = list(map(lambda x: x.upper(), countries))
print(countries_squared)
# 使用 map 将 numbers 列表中的每个数字更改为平方，生成一个新列表。
numbers_2 = list(map(lambda x: x ** 2, numbers))
print(numbers_2)
# 使用 map 将 names 列表中的每个名称更改为大写，生成一个新列表。
names_squared = list(map(lambda name: name.upper(), names))
print(names_squared)
# 使用 filter 过滤出包含“land”的国家。
countries_land = list(filter(lambda country: 'land' in country, countries))
print(countries_land)
# 使用 filter 过滤出正好六个字符的国家。
countries_6length = list(filter(lambda country: len(country) == 6, countries))
print(countries_6length)
# 使用 filter 过滤出包含六个字母及以上的国家。
countries_6length_more = list(filter(lambda country: len(country) > 6, countries))
print(countries_6length_more)
# 使用 filter 过滤出以'E'开头的国家。
countries_E = list(filter(lambda country: country[0] == 'E', countries))
print(countries_E)


# 链接两个或多个列表迭代器（例如 arr.map(callback).filter(callback).reduce(callback)）。

# 声明一个函数 get_string_lists，它接收一个列表作为参数并返回一个仅包含字符串项的列表。
def get_string_lists(lis: list):
    # string_lists = list(filter(lambda x:type(x)==str),lis)
    return [x for x in lis if isinstance(x, str)]


# 使用 reduce 对 numbers 列表中的所有数字求和。
total_numbers = int(reduce(lambda x, y: x + y, numbers))
print(total_numbers)
# 使用 reduce 将所有国家连接起来，生成句子：Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries。
# sentence = reduce(lambda x,y:f'{x},and {y}' if y == countries[-1] else f'{x}, {y}',countries)
previous_countries = countries[:-1]
last_country = countries[-1]
first_part = reduce(lambda x, y: f'{x}, {y}', previous_countries)
sentence = f"{first_part}, and {last_country} are north European countries"
print(sentence)
# 声明一个函数 categorize_countries，返回一个包含某种通用模式的国家列表（可以在本仓库的 countries.js 文件中找到国家列表，例如 'land', 'ia', 'island', 'stan'）。
import json
import os


def load_country_data():
    # 假设你的文件路径是 data/countries_data_long.json
    file_path = r'D:\DESKTOP\MyPythonStudy\30-Days-Of-Python\data\countries_data.json'

    # 检查文件是否存在，防止报错
    if not os.path.exists(file_path):
        print(f"❌ 错误：找不到文件 {file_path}")
        return []

    # 'r' 表示只读模式，encoding='utf-8' 防止中文或特殊字符乱码
    with open(file_path, 'r', encoding='utf-8') as f:
        # json.load 会自动把 json 格式转化为 Python 的 list 或 dict
        data = json.load(f)
        return data


def categorize_countries(pattern: str, country_lis=load_country_data()):
    country_pattern = [country['name'] for country in country_lis if pattern in country['name']]
    return country_pattern


land_country = categorize_countries('ina')
print(land_country)

import string


# 创建一个返回字典的函数，其中键表示国家名称的首字母，值表示以该字母开头的国家数。
def ABC_country(country_lis=load_country_data()):
    dic_ABC_country = {}
    for country in country_lis:
        dic_ABC_country[country['name'][0]] = dic_ABC_country.get(country['name'][0], 0) + 1
    return dic_ABC_country


# print(ABC_country())
from collections import Counter


def ABC_country_pro(country_lis=None):
    if country_lis is None:
        country_lis = load_country_data()

    # 1. 列表推导式提取首字母 (或者用 map)
    # initials = [country['name'][0].upper() for country in country_lis]
    initials = list(map(lambda x: x['name'][0].upper(), country_lis))
    # 2. 直接统计
    return dict(Counter(initials))


print(ABC_country_pro())

# 声明一个 get_first_ten_countries 函数 - 它返回数据文件夹中 countries.js 列表中的前十个国家。
def get_first_ten_countries(country_lis=None):
    if country_lis is None:
        country_lis = load_country_data()

    first_ten_countries = [country['name'] for country in country_lis[0:10]]
    return first_ten_countries
print(get_first_ten_countries())
# 声明一个 get_last_ten_countries 函数 - 它返回国家列表中的最后十个国家。
def get_last_ten_countries(country_lis=None):
    if country_lis is None:
        country_lis = load_country_data()
    last_ten_countries =  [country['name'] for country in country_lis[-10:]]
    return last_ten_countries
print(get_last_ten_countries())
# print(string.ascii_letters)
# 按国家名称、首都和人口排序国家
country_lis = load_country_data()
country_lis.sort(key = lambda x:x['population'],reverse = True)
print([(country['name'],country['population']) for country in country_lis[0:10]])

# 按位置排序出前十个最常用语言。
initials_language = [language for country in country_lis for language in country['languages']]
    # list(map(lambda x: x['languages'], country_lis))
# print(initials_language)
counter_language = Counter(initials_language)
Top10_language = counter_language.most_common(10)
print(Top10_language)
# 排序出前十个人口最多的国家。

print([(country['name'],country['population']) for country in country_lis[0:10]])

