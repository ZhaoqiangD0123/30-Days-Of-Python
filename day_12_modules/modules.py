from random import randint,random,sample
from my_modules import shuffle_list
import string


# 编写一个生成六位数/字符 random_user_id 的函数。
# 先创建所有字母与数字，然后利用randint在新建的数据库里面任取六位
def random_user_id():
    name = ''
    number_letter = string.ascii_letters + string.digits
    for i in range(6):
        name += number_letter[randint(0, len(number_letter))]
    print(name)


random_user_id()


# 修改上一个任务。声明一个名为 user_id_gen_by_user 的函数。它不接受任何参数，但接受两个输入。一个输入是字符的数量，另一个输入是应生成的 ID 数量。
# 在外面嵌套一个循环，确保生成的id数量，内循环确保id的长度
def user_id_gen_by_user(len_id:int,number_ID:int):
    name = ''
    number_letter = string.ascii_letters + string.digits
    for i in range(number_ID):
        for j in range(len_id):
            name += number_letter[randint(0, len(number_letter)-1)]
        print(name)
        name = ''

user_id_gen_by_user(16,5)


# 编写一个名为 rgb_color_gen 的函数。它将生成 RGB 颜色（每个值范围从 0 到 255）。
def rgb_color_gen():
    print(f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})')

rgb_color_gen()


# 调用你的函数 shuffle_list，它接受一个列表作为参数并返回一个打乱的列表。
lis = ['adf','addf',65,'cv','sa','fff']
print(shuffle_list(lis))
print(sample(lis,len(lis)))

# 编写一个函数，它在 0-9 的范围内返回七个随机数的数组。所有数字必须是唯一的。
def random_7number():
    num = [word for word in range(10)]
    num_random_7 = []
    for i in range(7):
        num_random_7.append(num.pop(randint(0,len(num)-1)))
    return num_random_7


# print(random_7number())

# a = 'asdf'



# print(a[1])
# print(type(string.ascii_letters + string.digits))
