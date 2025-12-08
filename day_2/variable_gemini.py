import math # 用于精确的 PI 值

# 第二天：30 Days of python programming

# --- 练习： 1级 (变量声明) ---

# 规范：将逻辑相关的变量分组声明
first_name, last_name, full_name = 'Ding', 'Zhaoqiang', 'DingZhaoqiang'
country, city = 'China', 'Xian'
age, year = 21, 2025
is_married, is_true, is_light_on = False, True, True


# --- 练习： 2级 (计算与类型检查) ---

print("\n--- 等级 2: 类型检查 ---")
print('first_name type is:', type(first_name))
# ... 打印其他变量的类型 ...
print('is_light_on type is', type(is_light_on)) # 变量间用空行分隔

len_first_name = len(first_name)
len_last_name = len(last_name)
print(f'\nfirst_name 的长度是: {len_first_name}')

# 比较长度
if len_first_name > len_last_name:
    print('first_name is longer')
elif len_first_name == len_last_name:
    print('first_name 的长度等于 last_name')
else:
    print('last_name is longer')


# --- 数学运算 ---
num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(f'\nTotal: {total}, Diff: {diff}, Product: {product}, Division: {division}')


# --- 圆的计算 (R=30m) ---
PI = math.pi
RADIUS = 30

area_of_circle = PI * RADIUS ** 2
circum_of_circle = 2 * PI * RADIUS

print(f'\n圆的面积: {area_of_circle:.2f} 平方米')
print(f'圆的周长: {circum_of_circle:.2f} 米')

# --- 用户输入计算面积 ---
# 始终假设用户输入有效，否则需要异常处理
user_radius_str = input("请输入圆的半径(m):")
try:
    user_radius = float(user_radius_str)
    user_area = PI * user_radius ** 2
    # 将半径作为用户输入并计算面积。并将值存储到 area_of_circle
    area_of_circle = user_area
    print(f'用户输入半径 {user_radius}m 的面积是: {area_of_circle:.2f} 平方米')
except ValueError:
    print('输入无效，请确保输入的是数字。')

# --- 获取用户信息 ---
# 声明新的变量来存储用户输入，避免覆盖原始变量
user_first_name = input('Please input your first name:')
user_last_name = input('Please input your last name:')
user_country = input('Please input your Country:')
user_age = int(input('Please input your age:')) # age 通常需要转换为整数

# --- 检查 Python 保留字 ---
print("\n--- Python 保留字 ---")
# 运行 help('keywords')
# help('keywords')