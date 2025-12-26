# 使用列表推导式过滤出列表中的负数和零：
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_zheng = [number for number in numbers if number > 0]
print(numbers_zheng)

# 将以下列表中的列表展平为一维列表：
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_number = [lis for lists in list_of_lists for list_row in lists for lis in list_row]
print(list_number)

# 使用列表推导式创建以下元组列表：
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
list_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
for row in list_tuples:
    print(row)
# 将以下列表展平成一个新列表：
countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
country = [[cou,cou[:1],city] for lis in countries for cou,city in lis]

# 输出:
# [['芬兰', '芬', '赫尔辛基'], ['瑞典', 'SWE', '斯德哥尔摩'], ['挪威', 'NOR', '奥斯陆']]
# 将以下列表转换为字典列表：
countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
countries_dic = [{'国家':cou,'城市':city} for lis in countries for cou,city in lis]
print(countries_dic)


# 输出:
# [{'国家': '芬兰', '城市': '赫尔辛基'},
# {'国家': '瑞典', '城市': '斯德哥尔摩'},
# {'国家': '挪威', '城市': '奥斯陆'}]



# 将以下列表转换为连接字符串的列表：
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

name_dic = [a +' '+ b for lis in names for a,b in lis]
print(name_dic)
# 输出:

# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']


