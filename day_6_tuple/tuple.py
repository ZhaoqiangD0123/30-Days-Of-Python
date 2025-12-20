# 创建一个空元组
empty_tuple = ()
# 创建一个包含你姐妹和兄弟名字的元组（虚构的兄弟姐妹也可以）
family_sister = ('Alice','Mark','Black')
family_brother = ('Alan','White')
# 连接兄弟姐妹元组并将其分配给 siblings
siblings = family_sister + family_brother
# 你有多少兄弟姐妹？
print(f'I have {len(siblings)} family numbers')
# 修改兄弟姐妹元组并添加你父母的名字，然后将其分配给 family_members
# list(family_sister).append('Uvan')
# list(family_brother).append('Nike')

# ('Uvan',) == tuple(['Uvan'])
family_sister = family_sister+('Uvan',)
family_brother = family_brother+('Nike',)
family_members = tuple(family_sister+family_brother)
family_members = list(family_members)
family_members[0:0] = ['Mother','Father']
family_members = tuple(family_members)
print(family_members)
# 从 family_members 中获取兄弟姐妹和父母
family_parents = family_members[0:2]
family_sister = family_members[2:3]
family_brother = family_members[3:]
# 创建 fruits、vegetables 和 animal products 元组。连接三个元组并将其分配给名为 food_stuff_tp 的变量。
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Lion','Monkey','Panda','Dog','Fox')
food_stuff_tp = fruits+vegetables+animal_products
# 将 food_stuff_tp 元组更改为 food_stuff_lt 列表
food_stuff_lt = list(food_stuff_tp)
# 从 food_stuff_tp 元组或 food_stuff_lt 列表中切出中间项或项。
food_stuff_tp_tap = food_stuff_tp[4:9]
print(food_stuff_tp_tap)
# 从 food_staff_lt 列表中切出前三项和最后三项
first_3 = food_stuff_lt[0:3]
last_3 = food_stuff_lt[-3:]
print(first_3)
print(last_3)
# 完全删除 food_staff_tp 元组
del food_stuff_tp
# 检查元组中是否存在项：
try:
    print(food_stuff_tp)
except:
    print('不存在项目了')
# 检查 'Estonia' 是否在 nordic_country 元组中
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'\'Estonia\'是否在 nordic_country: {"Estonia" in nordic_countries}')
# 检查 'Iceland' 是否在 nordic_country 元组中
print(f'\'Iceland\'是否在 nordic_country: {"Iceland" in nordic_countries}')
