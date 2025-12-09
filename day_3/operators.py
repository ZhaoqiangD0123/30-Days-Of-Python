import math
import pandas as pd
import numpy as np

# excise day_3
'''
声明一个值是你年龄的整型变量
声明一个值是你身高的浮点型变量
声明一个值是复数变量
'''
# age = 21  # year
# height = 1.7  # m
# complex_my = 1 + 1j
# # 编写一个脚本，提示用户输入三角形的底和高，并计算这个三角形的面积（面积 = 0.5 x b x h）。
# l = float(input("输入三角形的底："))
# h = float(input("输入三角形的高："))
# print('三角形的面积是：', l * h * 0.5)
#
# # 编写一个脚本，提示用户输入三角形的边 a、边 b 和边 c。计算三角形的周长（周长 = a + b + c）。
# a = float(input("输入边 a ："))
# b = float(input("输入边 b ："))
# c = float(input("输入边 c ："))
# perimeter_triangle = a + b + c
# print('三角形的周长是:', perimeter_triangle)
#
# # 提示用户输入矩形的长度和宽度。计算其面积（面积 = 长 x 宽）和周长（周长 = 2 x (长 + 宽)）
# length_rectangle = float(input("输入矩形的长："))
# width_rectangle = float(input("输入矩形的宽："))
# area_rectangle = length_rectangle * width_rectangle
# perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
# print('矩形的周长是:', perimeter_rectangle, '\n矩形的面积是:', area_rectangle)


# # 提示用户输入圆的半径。计算面积（面积 = pi x r x r）和周长（周长 = 2 x pi x r），其中 pi = 3.14。
# pi = math.pi
# r_circle = float(input('请输入圆的半径：'))
# area_circle = pi * r_circle * r_circle
# perimeter_circle = 2 * pi * r_circle
# print('圆的周长是:', perimeter_circle, '\n圆的面积是:', area_circle)

# # 计算 y = 2x -2 的斜率、x 截距和 y 截距
# x_0 = 0
# y_0 = 2 * x_0 - 2
# a = [x_0, y_0]
# y_1 = 0
# x_1 = (y_1 + 2) / 2
# b = [x_1, y_1]
#
# slope_ab = (b[1] - a[1]) / (b[0] - a[0])
# x_intercept = x_1
# y_intercept = y_0
#
# # 找到点 (2, 2) 和点 (6,10) 之间的斜率和欧几里得距离。
# c = [2, 2]
# d = [6, 10]
# slope_cd = (d[1] - c[1]) / (d[0] - c[0])
# Euclid_cd = math.sqrt((d[1] - c[1]) ** 2 + (d[0] + c[0]) ** 2)
# print('slope', c, d, ':', slope_cd)
# print('Euclid', c, d, ':', Euclid_cd)


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

# # 使用 and 运算符检查 'python' 和 'dragon' 中是否都有 'on'。
# if 'on' in 'python' and 'on' in 'dragon':
#     print(True)
# else:print(False)