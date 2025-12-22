# 分别使用while和for实现从0到10的迭代。
condition = 0
while condition <= 10:
    print(condition, end=' ')
    condition += 1
print()
for i in range(0, 11):
    print(i, end=' ')
print()
# 分别使用while和for实现从10到0的迭代。
condition = 10
while condition >= 0:
    print(condition, end=' ')
    condition -= 1
print()
for i in range(10, -1, -1):
    print(i, end=' ')
print()

# 写一个循环，调用7次print()函数，输出如下的三角形：
number = 1
while number <= 7:
    # for i in range(0, number):
    #     print('#', end='')
    print('#' * number)
    number += 1

i, j = 0, 0
for i in range(1, 8):
    for j in range(0, i):
        print('#', end='')
    print()

# 使用嵌套循环来实现下面的输出：
i, j = 0, 0
for i in range(1, 9):
    for j in range(1, 9):
        print('# ', end='')
    print()
# 使用循环实现下面格式的输出：
condition = 1
while condition <= 10:
    print(f'{condition} x {condition} = {condition * condition}')
    condition += 1
# 用for循环遍历列表['Python', 'Numpy','Pandas','Django', 'Flask']，并打印输出每个元素。
list_skill = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for word in list_skill:
    print(word, end=' ')
print()
# 用for循环从0到100遍历并且打印输出所有偶数。
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')
print()
# 用for循环从0到100遍历并且打印输出所有奇数
for i in range(0, 101):
    if i % 2 == 1:
        print(i, end=' ')
print()

# 使用for循环从0到100遍历并且输出所有数字的和。
total = 0
for i in range(0, 101):
    total += i
print(f'0到100的总和是{total}')

# 使用for循环从0到100遍历并且分别输出所有奇数和所有偶数的和。
total_odd = 0
total_even = 0
for i in range(0, 101):
    if i % 2 == 1:
        total_odd += i
    if i % 2 == 0:
        total_even += i
print(f'The sum of all odd numbers(奇数) is {total_odd}. And the sum of all even numbers(偶数) is {total_even}.')

# 有一个列表fruits = ['banana', 'orange', 'mango', 'lemon']，使用循环反转列表中的元素。
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
median = ' '
for i in range(len(fruits) // 2):
    median = fruits[i]
    fruits[i] = fruits[len(fruits) - i - 1]
    fruits[len(fruits) - i - 1] = median
# fruits = fruits[::-1]
# fruits.reverse()
print(fruits)
apple = 'Apple'
print(apple[::-1])

'''
今日总结：
#变量命名的大忌 (Key Point)
在 Python 中，sum 是一个内置函数
以后遇到求和的变量，建议命名为 total, total_sum, result 或者 sum_val。


# Pythonic (地道) 的写法： Python 的字符串支持乘法！'#' * 5 就会输出 #####。这样可以把内层循环直接消除，代码极简。

反转：
fruits = ['banana', 'orange', 'mango', 'lemon']
# 方法 1：切片法 (最常用，产生新列表)
reversed_fruits = fruits[::-1]
# 方法 2：原地反转法 (修改原列表)
fruits.reverse()




'''
