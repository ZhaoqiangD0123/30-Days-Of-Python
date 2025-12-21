# 使用 input 获取用户输入（例如：“输入你的年龄：”）。如果用户 18 岁或以上，给出反馈：你已经足够大，可以学习驾驶。如果未满 18 岁，则给出需要等待的年数。输出：
age_in = float(input('请输入你的年龄：\n'))
if age_in>= 18:
    print('你已经足够大，可以学习驾驶。')
else:
    print(f'你还需要{18-age_in}年才能学习驾驶')


# 使用输入提示从用户处获得两个数字。如果 a 大于 b，返回 a 大于 b，如果 a 小于 b，返回 a 小于 b，否则返回 a 等于 b。输出:
a = float(input('请输入a的值：\n'))
b = float(input('请输入b的值：\n'))
if a>b:
    print('a > b')
elif a<b:
    print('a < b')
else:
    print('a == b')

# 编写代码，根据学生的分数给出等级：
socre = float(input('输入你的分数：\n'))
if socre>=80:
    print('你的等级是A')
elif 70 <= socre < 80:
    print('你的等级是B')
elif 60 <= socre < 70:
    print('你的等级是C')
elif 50 <= socre < 60:
    print('你的等级是D')
else:
    print('你的等级是E')

# 检查是否是秋天、冬天、春天或夏天。如果用户输入： 9 月、10 月或 11 月，是秋天。 12 月、1 月或 2 月，是冬天。 3 月、4 月或 5 月，是春天。 6 月、7 月或 8 月，是夏天。
Month = int(input('输入月份：\n'))
if Month in [9,10,11]:
    print('是秋天')
elif Month in [12,1,2]:
    print('是冬天')
elif Month in [2,3,4]:
    print('是春天')
elif Month in [5,6,7]:
    print('是夏天')
else:
    print('输入错误')

# 以下列表包含了一些水果：
fruits = ['banana', 'orange', 'mango', 'lemon']
# 如果列表中不存在某个水果，则将其添加到列表中并打印修改后的列表。如果水果存在，则打印('该水果已在列表中')。
fruit = str(input('请输入一种水果:\n'))
if fruit in fruits:
    print('该水果已在列表中')
else:
    fruits.append(fruit)
    print('已将其添加进列表中')
print(fruits)

# 这里有一个人员字典。请随意修改它！
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '太空街',
        'zipcode': '02210'
    }
}
# 检查是否在字典中有 skills 键，如果有则打印 skills 列表中的中间技能。
try:
    print('存在skills，内容如下：\n', person['skills'])
except:
    print('不存在skills')
# 检查是否在字典中有 skills 键，如果有则检查该人是否具备'Python'技能并打印结果。
if person.get('skills') is not None:
    if 'Python' in person['skills']:
        print('该人具备"Python"技能')
    else:
        print('该人不具备"Python"技能')
else:
    print('不存在skills')
# 如果一个人的技能只有  和 React，打印('他是前端开发者')，如果一个人的技能有 Node、Python、MongoDB，打印('他是后端开发者')，如果一个人的技能有 React、Node 和 MongoDB，打印('他是全栈开发者')，否则打印'未知头衔' - 为获得更准确的结果，可以嵌套更多条件！
skills = set(person['skills'])
if {'React', 'Node', 'MongoDB'}.issubset(skills):
    print(person['first_name'] + person['last_name'] + '是一个全栈开发者')
elif {'Node','Python','MongoDB'}.issubset(skills):
    print(person['first_name'] + person['last_name'] + '是一个后端开发者')
elif {'JavaScript','React'}.issubset(skills):
    print(person['first_name'] + person['last_name'] + '是一个前端开发者')
else:
    print('未知头衔')
