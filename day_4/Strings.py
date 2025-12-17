# # 将字符串 'Thirty', 'Days', 'Of', 'Python' 连接为一个字符串 'Thirty Days Of Python'。
# print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
# a = 'Thirty'
# b = 'Days'
# c = 'Of'
# d = 'Python'
# e = ' '.join([a, b, c, d])
# print(e)

# # 将字符串 'Coding', 'For', 'All' 连接为一个字符串 'Coding For All'。
# 同上

# 声明一个名为 company 的变量，并将其赋值为初始值 "Coding For All"。
# 使用 print() 打印变量 company。
company = "Coding For All"

# print(company)
# # 使用 len() 方法和 print() 打印 company 字符串的长度。
# print(len(company))
# # 使用 upper() 方法将所有字符更改为大写字母。
# print(company.upper())
# # 使用 lower() 方法将所有字符更改为小写字母。
# print(company.lower())
# # 使用 capitalize()、title() 和 swapcase() 方法格式化字符串 Coding For All。
# print(company.capitalize())  # 首个字母大写
# print(company.title())  # 所有单词都是以大写开始，其余字母均为小写(
# print(company.swapcase())  # 将所有大写字符转换为小写字符，将所有小写字符转换为大写字符
#
# # 切片出 Coding For All 字符串的第一个单词。
# print(company.split()[0])
# print(company[0:6])
#
# # 使用 index、find 或其他方法检查 Coding For All 字符串是否包含单词 Coding。
# sub_str = 'Coding'
# if company.find(sub_str) != -1:
#     print('含有Coding')
# else:
#     print('不含有')
#
# try:
#     # 尝试直接获取
#     company.index(sub_str)
#     print('含有Coding')
# except ValueError:
#     # 如果报错了，代码会跳到这里执行，而不会崩溃
#     print('不含有')


# # 将字符串 'Coding For All' 中的单词 Coding 替换为 Python。
# print(company.replace('Coding', 'Python'))
#
# # 使用 replace 方法或其他方法将 Python for Everyone 替换为 Python for All。
# print('Python for Everyone'.replace('Everyone','All'))
#
# # 使用空格作为分隔符拆分字符串 'Coding For All'
# print(company.split(' '))
#
# # 在逗号处拆分字符串 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'。
# print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
#
# # 字符串 Coding For All 中索引 0 处的字符是什么。
# print(company[0])
#
# # 字符串 Coding For All 的最后一个索引是什么。
# print(company[-1])
#
# # 字符串 Coding For All 中索引 10 处的字符是什么。
# print(company[10])
#
# # 为字符串 'Python For Everyone' 创建首字母缩略词或缩写
#
# # 为名称 'Coding For All' 创建首字母缩略词或缩写。
# # 定义目标字符串
# str1 = 'Python For Everyone'
# str2 = 'Coding For All'
#
# # --- 方法 1：使用列表推导式 (推荐，一行代码搞定) ---
# # 逻辑：对于 text 拆分后的每一个 word，取出它的第0个字符，然后拼接
# acronym1 = ''.join([word[0] for word in str1.split()]).upper()
# acronym2 = ''.join([word[0] for word in str2.split()]).upper()
#
# print(f"1. '{str1}' 的缩写为: {acronym1}")
# print(f"2. '{str2}' 的缩写为: {acronym2}")
# # 使用索引确定 'Coding For All' 中 C 第一次出现的位置。
# print(f"第一次出现的位置是下标{company.find('F')} ")

# # 为名称 'Coding For All' 创建首字母缩略词或缩写。
# str3 = 'Coding For all'
# acronym3 = ''.join([word[0] for word in str3.split()]).upper()
#
# print(acronym3)


# 使用 rfind 确定 'Coding For All People' 中 l 最后一次出现的位置。
print(f"最后第一次'l'出现的位置是下标{company.rfind('l')} ")

# 使用 index 或 find 查找以下句子中单词 'because' 第一次出现的位置：'You cannot end a sentence with because because because is a conjunction'
str1 = 'You cannot end a sentence with because because because is a conjunction'
print(str1.find('because'))

# 使用 rindex 查找以下句子中单词 because 最后一次出现的位置：'You cannot end a sentence with because because because is a conjunction'
str2 = 'You cannot end a sentence with because because because is a conjunction'
print(str2.rfind('because'))

# 删除以下句子中短语 'because because because'：'You cannot end a sentence with because because because is a conjunction'
print(str2.replace('because ', ''))

# 'Coding For All' 是否以子字符串 Coding 开头？
str3 = 'Coding For All'
print(str3.startswith('Coding'))

# 'Coding For All' 是否以子字符串 coding 结尾？
print(str3.endswith('coding'))
# '   Coding For All      '  , 删除给定字符串中左右空格。
str4 = '   Coding For All      '
print(str4.strip())  # !!!!
# 当我们使用方法 isidentifier() 时，下列哪一个变量返回 True：判断是否是一个有效的标识符
# 30DaysOfPython
# thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
# 以下列表包含一些 Python 库的名称：['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']。使用空格连接字符串。

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
acc = ' '.join([word for word in list1])
print(acc)

# 使用换行转义序列分隔以下句子。
# I am enjoying this challenge.
# I just wonder what is next.

s1 = 'I am enjoying this challenge.'
s2 = 'I just wonder what is next.'
s3 = s1 + '\n' + s2
print(s3)
# 使用制表符专业序列输出以下内容。
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("{:<12} {:<8} {:<12} {}".format('Name', 'Age','Country','City'))
print("{:<12} {:<8} {:<12} {}".format("Asabeneh", "250", "Finland", "Helsinki"))


# 使用字符串格式化方法输出以下内容:
radius = 10
area = 3.14 * radius **2
# The area of a circle with radius 10 is 314 meters square.
print("radius = {}\narea = 3.14 * radius **2\nThe area of a circle with radius {} is {} meters square.".format(radius,radius,area))
# 使用字符串格式化方法输出以下内容:
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')







