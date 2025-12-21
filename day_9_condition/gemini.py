# --- 成绩分级 (优化版) ---
score = float(input('输入你的分数：\n')) # 修正拼写 socre -> score
if score >= 80:
    print('你的等级是A')
elif score >= 70: # 移除多余的范围判断
    print('你的等级是B')
elif score >= 60:
    print('你的等级是C')
elif score >= 50:
    print('你的等级是D')
else:
    print('你的等级是E')

# --- 季节判断 (修正月份重叠) ---
month = int(input('输入月份：\n'))
if month in [9, 10, 11]:
    print('是秋天')
elif month in [12, 1, 2]:
    print('是冬天')
elif month in [3, 4, 5]: # 修正范围，去掉重复的 2
    print('是春天')
elif month in [6, 7, 8]: # 修正范围
    print('是夏天')
else:
    print('输入错误')

# --- 字典与开发者判定 (逻辑精修) ---
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    # ... 其他数据保持不变 ...
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
}

# 1. 找中间技能
# 建议用 if 检查键是否存在，比 try-except 更符合语境
if 'skills' in person:
    skills_list = person['skills']
    mid = len(skills_list) // 2
    print(f"中间技能是: {skills_list[mid]}")
else:
    print('不存在skills')

# 2. 判定职位 (Set 逻辑优化)
# 先把列表转成集合，方便计算
person_skills = set(person['skills'])
full_name = f"{person['first_name']} {person['last_name']}" # 使用 f-string 自动加空格

# 定义职位要求的集合
frontend_req = {'JavaScript', 'React'}
backend_req = {'Node', 'Python', 'MongoDB'}
fullstack_req = {'React', 'Node', 'MongoDB'}

if frontend_req == person_skills: # 题目要求"只有"，所以用 ==
    print(f'{full_name} 是一个前端开发者')
elif fullstack_req.issubset(person_skills): # 包含这些就是全栈
    print(f'{full_name} 是一个全栈开发者')
elif backend_req.issubset(person_skills):   # 包含这些就是后端
    print(f'{full_name} 是一个后端开发者')
else:
    print('未知头衔')