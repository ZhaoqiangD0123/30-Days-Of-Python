import sys
import math # 导入 math 模块用于欧几里得距离计算

# --- 练习：等级 2 (计算与类型检查) ---

# 1. 检查 Python 版本
version_info = sys.version_info
print(f"当前 Python 版本: {version_info.major}.{version_info.minor}.{version_info.micro}")

# 2. 基本数学运算 (操作数 3 和 4)
print("\n--- 等级 2: 数学运算 ---")
print(f"加法 (+): 3 + 4 = {3 + 4}")
print(f"减法 (-): 3 - 4 = {3 - 4}")
print(f"乘法 (*): 3 * 4 = {3 * 4}")
print(f"取模 (%): 3 % 4 = {3 % 4}")
print(f"除法 (/): 3 / 4 = {3 / 4}")
print(f"指数 (**): 3 ** 4 = {3 ** 4}")
print(f"整除 (//): 3 // 4 = {3 // 4}")

# 3. 打印字符串
print("\n--- 等级 2: 字符串 ---")
print('Zhaoqiang')
print('Ding')
print('China')
print('I am enjoying the 30 days of python')

# 4. 数据类型检查
print("\n--- 等级 2: 类型检查 ---")
print(f"10 的数据类型是: {type(10)}")
print(f"9.8 的数据类型是: {type(9.8)}")
print(f"3.14 的数据类型是: {type(3.14)}")
print(f"4 - 4j 的数据类型是: {type(4 - 4j)}")
print(f"['Asabeneh', 'Python', 'Finland'] 的数据类型是: {type(['Asabeneh','Python','Finland'])}")
# 字符串类型检查... (后续省略)


# --- 练习：等级 3 (数据类型示例与距离计算) ---

# 1. 为不同数据类型编写示例 (通过变量赋值实现)
print("\n--- 等级 3: 数据类型示例 ---")
integer_var = 100            # 整数
float_var = 3.14159          # 浮点数
complex_var = 5 + 2j         # 复数
string_var = "Hello Python"  # 字符串
boolean_var = True           # 布尔值
list_var = [1, "two", 3.0]   # 列表
tuple_var = (1, 2, 3)        # 元组
set_var = {1, 2, 3, 3}       # 集合 (自动去重)
dict_var = {'key': 'value', 'age': 30} # 字典

print(f"整数示例: {integer_var}")
print(f"列表示例: {list_var}")
# ... 打印其他变量 ...


# 2. 欧几里得距离计算：(2, 3) 和 (10, 8)
a = (2, 3)
b = (10, 8)

# 正确的欧几里得距离计算公式实现
distance = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

print(f"\n点 a{a} 和 点 b{b} 之间的欧几里得距离: {distance}")