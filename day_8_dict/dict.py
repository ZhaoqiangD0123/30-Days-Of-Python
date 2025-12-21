# 创建一个名为 dog 的空字典
dog = {}# dog = dict()
# 向 dog 字典添加 name、color、breed、legs、age 键
dog['name'] = 'Bili'
dog['color'] = 'Black'
dog['breed'] = 'None'
dog['legs'] = 'OK'
dog['age'] = '5'
print(dog.items())
# 创建一个学生字典，添加 first_name、last_name、gender、age、marital status、skills、country、city 和 address 作为字典的键
student = {
    'first_name' : 'Ding',
    'last_name':'Zhaoqiang',
    'gender':'Man',
    'age':21,
    'marital status':None,
    'skills':['Run','Reading'],
    'country':'China',
    'city':'Anhui',
    'address':'BoZhou'
}
# 获取学生字典的长度
print(len(student))
# 获取 skills 的值并检查数据类型，应该是列表
print(student.get('skills'))
print(type(student['skills']))
# 修改 skills 值，添加一到两个技能
student['skills'].extend(['Walk','keep'])
print(student['skills'])
# 获取字典的键列表
print(student.keys())
# 获取字典的值列表
print(student.values())
# 使用 items() 方法将字典变为由元组组成的列表
list_student = list(student.items())
print(list_student)
# 删除字典中的一项
student.pop('skills')
print(student)
# 删除其中一个字典
del dog
try:
    print(dog)
except:
    print('不存在“dog”')


