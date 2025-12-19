# --- Level 1 ---
# 1. 创建空元组
empty_tuple = ()

# 2. 创建兄弟姐妹元组
family_sister = ('Alice', 'Mark', 'Black')
family_brother = ('Alan', 'White')

# 3. 连接元组
siblings = family_sister + family_brother

# 4. 打印数量
print(f'I have {len(siblings)} family members') # 修正拼写 numbers -> members

# 5. 修改元组 (关键修正)
# 思路：元组不能改 -> 转成列表 -> 改列表 -> 转回元组
siblings_list = list(siblings)
# 添加父母名字到列表中 (比如加到开头)
siblings_list.insert(0, 'Father')
siblings_list.insert(0, 'Mother')
family_members = tuple(siblings_list)

print("家庭成员:", family_members)

# --- Level 2 ---
# 1. 创建食物元组
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('Meat', 'Milk', 'Honey') # 这里通常指产品，不过用动物名也可以

# 2. 连接
food_stuff_tp = fruits + vegetables + animal_products

# 3. 转列表
food_stuff_lt = list(food_stuff_tp)

# 4. 切出中间项 (动态计算，更通用)
n = len(food_stuff_lt)
middle_index = n // 2 # 整除
# 如果是想取中间的那一个：
print(f"中间项是: {food_stuff_lt[middle_index]}")
# 如果是想取中间的一段（例如中间由两项组成，或者取中间附近）：
print(f"中间切片: {food_stuff_lt[middle_index-1 : middle_index+1]}")

# 5. 前三项和后三项
first_3 = food_stuff_lt[:3]  # 0可以省略
last_3 = food_stuff_lt[-3:]
print(f"前三: {first_3}")
print(f"后三: {last_3}")

# 6. 删除元组
del food_stuff_tp

# 7. 检查是否存在
try:
    print(food_stuff_tp)
except NameError: # 最好指定具体的错误类型 NameError
    print('food_stuff_tp 已被删除，无法读取。')

# 8. 检查元素是否存在
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
check_estonia = 'Estonia' in nordic_countries
check_iceland = 'Iceland' in nordic_countries

print(f"'Estonia' is a nordic country: {check_estonia}")
print(f"'Iceland' is a nordic country: {check_iceland}")