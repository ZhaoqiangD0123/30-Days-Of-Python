import sys

#print(version)

'''
1.检查你使用的 Python 版本
2.打开 Python 交互式 Shell 并执行以下操作。操作数是 3 和 4。
加法(+)
减法(-)
乘法(*)
取模(%)
除法(/)
指数(**)
整除(//)
3.在 Python 交互式 Shell 中编写字符串。字符串如下：
你的名字
你的姓氏
你的国家
我正在享受 30 天的 Python
4.检查以下数据的数据类型：
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
你的名字
你的姓氏
你的国家
'''
version_info = sys.version_info
print(f"当前 Python 版本: {version_info.major}.{version_info.minor}.{version_info.micro}")

print(3+4)#addition
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)


print('Zhaoqiang')
print('Ding')
print('China')
print('I am enjoying the 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type('Zhaoqiang'))
print(type('Ding'))
print(type('China'))

'''
1.为不同的 Python 数据类型编写一个示例，如数字（整数、浮点数、复数）、字符串、布尔值、列表、元组、集合和字典。
2.找到 (2, 3) 和 (10, 8) 之间的 欧几里得距离。
'''
print('''数字
整数：它被认为是整数（负数、零和正数） 示例： ... -3, -2, -1, 0, 1, 2, 3 ...
浮点数：小数 示例： ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
复数 示例： 1 + j, 2 + 4j''')

print('''字符串
一串字符组成的文本，使用单引号或双引号表示。如果字符串超过一行，可以使用三引号。
例子:
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
''')
print('''布尔值
布尔值是 True 或 False。T 和 F 必须大写。
例子:
True # 灯是开的吗？如果是开着的，那么值是 True
False # 灯是开的吗？如果是关着的，那么值是 False
''')

print('''列表
列表是一个有序的集合，可以存储不同类型的数据。类似于 JavaScript 中的数组。
例子:
[0, 1, 2, 3, 4, 5] # 所有都是相同数据类型 - 数字列表
['Banana', 'Orange', 'Mango', 'Avocado'] # 所有都是相同数据类型 - 字符串列表（水果）
['Finland','Estonia', 'Sweden','Norway'] # 所有都是相同数据类型 - 字符串列表（国家）
['Banana', 10, False, 9.81] # 列表中的不同数据类型 - 字符串、整数、布尔值和浮点数
''')
print('''字典
Python 字典对象是以键值对格式存储的无序集合。
例子:
{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland',
'age':250,
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
        ''')
print('''元组
元组是一个有序的集合，类似于列表，但元组一旦创建就不能修改。它们是不可变的。
例子:
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # 名字
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # 行星
      ''')
print('''集合
集合是类似于列表和元组的集合数据类型。与列表和元组不同，集合不是一个有序的集合。就像在数学中一样，Python 中的集合只存储唯一的项目。
例子:
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # 集合中的顺序不重要
    ''')
a = (2, 3)
b = (10, 8)
Euclidean_distance = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
print(f"(2, 3)与(10, 8)的欧几里得距离：Euclidean_distance={Euclidean_distance}")


