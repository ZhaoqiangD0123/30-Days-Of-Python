import math
import pandas as pd
import numpy as np

# excise day_3
'''
声明一个值是你年龄的整型变量
声明一个值是你身高的浮点型变量
声明一个值是复数变量
'''
age = 21  # year
height = 1.7  # m
complex_my = 1 + 1j
# 编写一个脚本，提示用户输入三角形的底和高，并计算这个三角形的面积（面积 = 0.5 x b x h）。
l = float(input("输入三角形的底："))
h = float(input("输入三角形的高："))
print('三角形的面积是：', l * h * 0.5)

# 编写一个脚本，提示用户输入三角形的边 a、边 b 和边 c。计算三角形的周长（周长 = a + b + c）。
a = float(input("输入边 a ："))
b = float(input("输入边 b ："))
c = float(input("输入边 c ："))
perimeter_triangle = a + b + c
print('三角形的周长是:', perimeter_triangle)

# 提示用户输入矩形的长度和宽度。计算其面积（面积 = 长 x 宽）和周长（周长 = 2 x (长 + 宽)）
length_rectangle = float(input("输入矩形的长："))
width_rectangle = float(input("输入矩形的宽："))
area_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print('矩形的周长是:', perimeter_rectangle, '\n矩形的面积是:', area_rectangle)

# 提示用户输入圆的半径。计算面积（面积 = pi x r x r）和周长（周长 = 2 x pi x r），其中 pi = 3.14。
pi = math.pi
r_circle = float(input('请输入圆的半径：'))
area_circle = pi * r_circle * r_circle
perimeter_circle = 2 * pi * r_circle
print('圆的周长是:', perimeter_circle, '\n圆的面积是:', area_circle)

# 计算 y = 2x -2 的斜率、x 截距和 y 截距
x_0 = 0
y_0 = 2 * x_0 - 2
a = [x_0, y_0]
y_1 = 0
x_1 = (y_1 + 2) / 2
b = [x_1, y_1]

slope_ab = (b[1] - a[1]) / (b[0] - a[0])
x_intercept = x_1
y_intercept = y_0

# 找到点 (2, 2) 和点 (6,10) 之间的斜率和欧几里得距离。
c = [2, 2]
d = [6, 10]
slope_cd = (d[1] - c[1]) / (d[0] - c[0])
Euclid_cd = math.sqrt((d[1] - c[1]) ** 2 + (d[0] + c[0]) ** 2)
print('slope', c, d, ':', slope_cd)
print('Euclid', c, d, ':', Euclid_cd)


# 计算 y 的值（y = x^2 + 6x + 9）。尝试使用不同的 x 值，并找出 y 何时为 0。
# 定义函数
def calculate_y(x):
    return x ** 2 + 6 * x + 9


# 创建测试的 x 值
x_values = np.arange(-6, 1, 1)
# 计算对应的 y 值
y_values = [calculate_y(x) for x in x_values]

# 结果可视化
results_df = pd.DataFrame({'x': x_values, 'y = x^2 + 6x + 9': y_values})

# 找出 y 为 0 的 x 值
y_is_zero = results_df[results_df['y = x^2 + 6x + 9'] == 0]

print(results_df)
print("\nWhere y is 0:")
print(y_is_zero)

# 使用 and 运算符检查 'python' 和 'dragon' 中是否都有 'on'。
if 'on' in 'python' and 'on' in 'dragon':
    print(True)
else:
    print(False)

# 找到文本 python 的长度，并将该值转换为浮点数，然后将其转换为字符串。
length_txt_int = len('python')
l_float = float(length_txt_int)
l_str = str(l_float)
print('length_txt_int', length_txt_int, type(length_txt_int))
print('l_float', l_float, type(l_float))
print('l_str', l_str, type(l_str))

# 偶数可以被 2 整除，余数为零。如何使用 Python 检查一个数字是偶数还是奇数？
num_int = int(input('请输入一个整数：\n'))
if num_int % 2 == 0:
    print(num_int, '是一个偶数')
else:
    print(num_int, '不是一个偶数')

# 检查 7 除以 3 的Floor除法是否等于 2.7 的整数转换值。
if 7 // 3 == int(2.7):
    print('7 除以 3 的Floor除法等于 2.7 的整数转换值')
else:
    print('7 除以 3 的Floor除法不等于 2.7 的整数转换值')

# 检查 '10' 的类型是否等于 10 的类型。

if type('10') == type(10):
    print(' ''10'' 的类型等于 10 的类型')
else:
    print(' ''10'' 的类型不等于 10 的类型')

# 检查 int('9.8') 是否等于 10。
if type('9.8') == 'int':
    if int('9.8') == 10:
        print('int(''9.8'') 等于 10')
    else:
        print('int(''9.8'') 不等于 10')
else:
    print('无法比较')

# 编写一个脚本，提示用户输入工时和时薪。计算用户的工资。
work_time = int(input('请输入你的工时：\n'))
pay_per_time = int(input('请输入你的时薪：\n'))
print('你的工资是：', work_time * pay_per_time)

# 编写一个脚本，提示用户输入年数。计算一个人还可以活多少秒。假设一个人可以活一百年
now_year = int(input('请输入当前年龄：'))
if now_year >= 100:
    print('超出年限')
else:
    residue_life = (100 - now_year) * 365 * 24 * 60 * 60
    print('你还能够活', residue_life, 's')

# 编写一个 Python 脚本，显示以下表格
tab = [1, 1, 1, 1, 1, 2, 1, 2, 4, 8, 3, 1, 3, 9, 27, 4, 1, 4, 16, 64, 5, 1, 5, 25, 125]
for i in range(0, 5):
    for j in range(0, 5):
        print(tab[i * 5 + j], end=' ')
    print()
