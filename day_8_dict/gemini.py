# --- Dog Dictionary ---
dog = {}
dog['name'] = 'Bili'
dog['color'] = 'Black'
dog['breed'] = 'Poodle' # 贵宾犬
dog['legs'] = 4   # 建议用整数
dog['age'] = 5    # 建议用整数
print(f"Dog Info: {dog.items()}")

# --- Student Dictionary ---
student = {
    'first_name': 'Ding',
    'last_name': 'Zhaoqiang',
    'gender': 'Man',
    'age': 21,
    'marital_status': 'Single', # 建议合并为一个键
    'skills': ['Run', 'Reading'],
    'country': 'China',
    'city': 'Anhui',
    'address': 'BoZhou'
}

# 1. 长度
print(f"字典长度: {len(student)}")

# 2. 获取技能并检查类型
skills = student.get('skills')
print(f"技能: {skills}, 类型: {type(skills)}")

# 3. 修改技能 (你的 extend 用得很棒！)
student['skills'].extend(['Walk', 'Coding'])
print(f"更新后的技能: {student['skills']}")

# 4. 键、值、项 (注意这里加了 list() 转换)
keys_list = list(student.keys())
values_list = list(student.values())
items_list = list(student.items())

print(f"Keys: {keys_list}")
print(f"Items (作为列表): {items_list}")

# 5. 删除项
removed_skill = student.pop('skills') # pop 会返回被删除的值，有时很有用
print(f"删除了技能列, 剩余字典: {student}")

# 6. 删除字典
del dog
try:
    print(dog)
except NameError: # 建议指明具体的错误类型
    print('字典 "dog" 已被删除，无法读取。')