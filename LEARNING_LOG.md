# Day [X]: [主题，模版]

## 1. 🧠 核心概念 (一句话总结)
* **概念 1**: [在这里写下关键知识点，例如：range() 的第三个参数是步长]
* **概念 2**: [例如：字典的 Key 必须是唯一的，但 Value 可以重复]

## 2. 💣 踩坑记录 (Error Log)
> 记录报错或逻辑错误，防止下次再犯。

* **错误现象**: [例如：使用了内置函数名 sum 作为变量名]
* **原因分析**: [例如：覆盖了全局函数，导致后续无法求和]
* **解决方案**: [例如：改名为 total_sum]

## 3. 代码进化 (Before vs After)
> 对比修改前后的代码，体会 Pythonic 的写法。

**Before (初版/啰嗦):**
```python
# [在这里粘贴你原本写的代码]
```
**After (进阶/优雅):**
```Python
# [在这里粘贴优化后的代码]
```
## 4. 📏 规范备忘录 (Style Guide)
> 每次写代码前看一遍，争取不再犯！
- [ ] 变量名绝对不能使用内置函数名（如 `sum`, `list`, `str`）。
- [ ] 涉及排名/排序时，不要把字典的 Key 和 Value 拆开，防止数据错位。
- [ ] 想要从列表里筛选数据时，优先尝试“列表推导式”写法。


### 💡 使用小贴士
1.  **复制**上面的内容。
2.  **粘贴**到你的 `LEARNING_LOG.md` 文件里。
3.  把 `[ ]` 里的内容替换成你今天的真实感悟。
4.  以后每一天学习新内容，就在文件最上面（或者最下面）复制一份这个模板，填入新的内容即可。


---
# Day 10: 循环Loops

## 🧠 核心概念 (一句话总结)
* **概念 1**: [**while循环，条件满足一直循环** ]
```Python
while condition:
    代码块
condition为True时，代码块运行
```
* **概念 2**: [**for循环：本质是对序列的遍历（也就是列表、元组、字典、集合、字符串等）。**]
```Python
for iterator in lst:
    代码块
```
* **概念 3**: [**break:终止此次大循环**]
* **概念 4**: [**continue:跳过此次小循环，此次循环中continue后面的代码块也不执行**]
## 每日Tips
> 记录一些错误与代码技巧
### 变量命名的大忌 (Key Point)
``
在 Python 中，sum 是一个内置函数
以后遇到求和的变量，建议命名为 total, total_sum, result 或者 sum_val。
``
### # Pythonic (地道) 的写法： 字符串乘法
Python 的字符串支持乘法！'#' * 5 就会输出 #####。
```Python
print('*' * 5) # *****
```
### 对一个列表或者字符串，将其反转的高级写法[::-1]/.reverse()
```Python
fruits = ['banana', 'orange', 'mango', 'lemon']
# 方法 1：切片法 (最常用，产生新列表)
reversed_fruits = fruits[::-1] # reversed_fruits = ['apple', 'lemon', 'mango', 'orange', 'banana']
# 方法 2：原地反转法 (修改原列表)
fruits.reverse() # fruits = ['apple', 'lemon', 'mango', 'orange', 'banana']

apple = 'Apple'
print(apple[::-1])
# elppA
```
### “列表推导式 (List Comprehension)”：🚀进阶写法
```Python
land_country = []
for country in countries:
    if 'land' in country:
        land_country.append(country)
#等价于       
land_country = [country for country in countries if 'land' in country]
```
### 字典.get(key, value(init))用法
```
counts = {}
for country in countries_data:
    for language in country['languages']:
        # 如果存在就+1，不存在就默认取0再+1
        counts[language] = counts.get(language, 0) + 1
```
---
### 例题求解：
1. 跳转到data文件夹并使用[countries_data.py]文件。
   1. 数据中一共有多少个语言？
   2. 找到被最多国家使用的语言。
   3. 找到人数排名前十的国家。
```
countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    }....
]
```
#### 我的求解：
```
# 跳转到data文件夹并使用countries_data.py文件。
# 数据中一共有多少个语言？
language_set = set()
for country_dic in countries_data:
    language_list = country_dic.get('languages')
    language_set.update(language_list)
print(len(language_set))
# 找到被最多国家使用的语言。
language_total_list = list(language_set)
language_total_dict = dict()
for language in language_total_list:
    language_total_dict[language] = 0
print(len(language_total_dict))
# print(language_total_dict.keys())
for country_dic in countries_data:
    language_list = country_dic.get('languages')
    for language in language_list:
        language_total_dict[language] += 1

max_language = 0
max_country = ''
for i in language_total_dict:
    if language_total_dict[i] > max_language:
        max_country = i
        max_language = language_total_dict[i]
print(f'被最多国家使用的语言是{max_country},次数是{max_language}')

# for language in language_list:
#     for country_dic in countries_data:
#         language_list = country_dic.get('languages')
#         language_set.update(language_list)
# print(len(language_set))

# 找到人数排名前十的国家。
count = 10
min_people = 0
countries_people = []
new_population_name_dict = dict()
for country_dic in countries_data:
    new_population_name_dict[str(country_dic['population'])] = country_dic['name']
    countries_people.append(country_dic['population'])
countries_people.sort(reverse=True)
countries_people = countries_people[0:10]

# print(len(new_population_name_dict))
print(countries_people)
for population in countries_people:
    print(new_population_name_dict[str(population)],end=', ')
```
#### 存在的问题：
````
我的思路是：
建立一个字典：key=人口数, value=国家名。
对人口数列表进行排序。
拿着排好序的人口数，去字典里查国家名。
❌ 致命隐患：Key 必须唯一 在字典中，Key 是唯一的。 假设（虽然概率很低）有两个国家人口正好都是 10000 人：
程序读到国家 A (10000人) -> 字典存 {'10000': 'A'}
程序读到国家 B (10000人) -> 字典更新 {'10000': 'B'} (A 被覆盖并消失了！)
当你后面排序取前十时，你可能少了一个国家，或者数据对应错了。绝对不要用可能重复的数据（如年龄、分数、人口、工资）作为字典的 Key。
````
#### 改进思路1：不要把人口和名字拆开，而是把它们绑定在一起处理。
#### 关键点：元组排序默认比较第一个[（53（int）,'China'）,（59（int）,'American'）]
```
使用元组列表 (Tuple List) - 推荐初学者 创建一个列表，
里面存 (人口, 国家名) 的元组，然后直接对这个列表排序。
# 1. 创建一个列表，存 (人口, 名字)
pop_list = []
for country in countries_data:
    pop_list.append((country['population'], country['name']))

# 2. 排序 (默认会先比较第一个元素，也就是人口)
# reverse=True 表示从大到小
pop_list.sort(reverse=True)

# 3. 切片取前10
top_10 = pop_list[:10]
# top_10 = [(1377422166, 'China'), (1295210000, 'India'), (323947000, 'United States of America'), (258705000, 'Indonesia'), (206135893, 'Brazil'), (194125062, 'Pakistan'), (186988000, 'Nigeria'), (161006790, 'Bangladesh'), (146599183, 'Russian Federation'), (126960000, 'Japan')]
# 4. 打印
for pop, name in top_10:
    print(f'{name}: {pop}')
```
#### 方法2：方法二：直接对字典列表排序 (lambda 表达式) - 进阶 这就用到了 sort 函数的高级用法 key 参数。
意思是：“请根据每个字典里的 'population' 键来帮我排队”。
```
# 根据 population 进行降序排序
countries_data.sort(key=lambda x: x['population'], reverse=True)

# 取前10个字典
for i in range(10):
    print(f"{countries_data[i]['name']} - {countries_data[i]['population']}")

```
这段代码是 Python 数据处理中最经典、最高效的写法之一。

 它涉及到了三个核心知识点：
1. **列表排序 (.sort())**
2. **关键字参数 (key=)**
3. **匿名函数 (lambda) —— 这是最难懂的部分。**
```
countries_data.sort(key=lambda x: x['population'], reverse=True)
```
这句话的意思是：“请把 countries_data 列表里的国家排个序，排序的标准是‘人口数量’，并且要从大到小排。”

1. ：**.sort() vs reverse=True**
* ``countries_data.sort():`` 这是一个原地修改的方法。它不创建新列表，而是直接改变原列表里的顺序。
* ``reverse=True: ``默认排序是从小到大（升序），加了这个参数就变成了从大到小（降序）。

2. ：**key 是什么？**

列表里装的是字典，不是简单的数字。
* 如果你让 Python 排序 [3, 1, 2]，它知道怎么排。
* 但如果你让它排序 [{'name':'China'}, {'name':'US'}]，Python 会懵圈：“大哥，你让我比什么？比名字长度？比首字母？还是比什么？”

key 就是用来告诉 Python：“别瞎猜，就比这个！”
3. ：**lambda x: x['population'] (重点！🔥)**

这是一个 Lambda 函数（匿名函数）。你可以把它看作是一个一次性的小工具。
* lambda: 告诉 Python 我要定义一个简单的函数。
* x: 这是函数的参数。在这里，x 代表列表中的每一个字典元素（就像 for 循环里的那个变量一样，你把它叫 country 也可以）。
* :: 分隔符。
* x['population']: 这是返回值。意思是我要把这个字典里的 'population' 值取出来，作为排序的依据。
如果不写 Lambda，代码会写成这样（完全等价）：
```
# 1. 先定义一个普通的函数，专门用来提取人口
def get_population(country_dict):
    return country_dict['population']

# 2. 告诉 sort 方法：用上面那个函数来决定顺序
countries_data.sort(key=get_population, reverse=True)
```
#### 💡 总结
 这行代码 countries_data.sort(key=lambda x: x['population'], reverse=True) 是处理复杂列表排序的标准答案。
 **什么时候用？** 当你有一个列表，里面装的是**字典**或**元组**，而你想根据里面的某一个字段进行排序时。
---

# Day 11: 函数与防御性编程

## 1. 🧠 核心概念
* **`*args`**: 用于接收不定数量的参数，在函数内部它是一个元组。
* **`all()` 函数**: Python 的神级内置函数，用于判断“是不是全都满足条件”，比手写 for 循环判断更优雅。
* **无副作用 (No Side Effects)**: **检查类**的函数（如 check_type）绝对不能修改传入的列表（如排序），否则会破坏原始数据。

## 2. 💣 踩坑记录 (Error Log)
* **错误现象**: `ZeroDivisionError: division by zero`
* **原因分析**: 计算斜率 `k = -a / b` 时，没有检查 `b` 是否为 0。
* **解决方案**: 在除法前必须加 `if b == 0:` 的卫语句判断。

* **错误现象**: 列表顺序莫名其妙变了。
* **原因分析**: 在做类型检查时使用了 `lis.sort()`，导致原列表被原地排序。
* **解决方案**: 避免使用 `sort` 做检查，或使用 `sorted(lis)` 创建新列表（但更推荐用 `all()`）。

## 3. 💅 代码进化 (Before vs After)

**检查全类型一致 (Before):**
```python
# 这种写法既慢又破坏数据
def is_only_type_list(lis):
    lis.sort(key=lambda x: str(type(x))) # ❌ 修改了原列表！
    return str(type(lis[0])) == str(type(lis[-1]))
  # 优雅、快速、无副作用
def is_only_type_list(lis):
    # 取第一个元素的类型做标尺
    return all(isinstance(x, type(lis[0])) for x in lis)
 ```
## Tips 列表推导式



# Day 11 (Advanced): 性能优化与副作用

## 1. 🧠 核心概念
* **`list.count()` 的性能陷阱**: 在循环里使用 `.count()` 会导致程序极慢 ($O(N^2)$)。统计数量时，永远优先考虑 **字典 (Dict)** 或 **`collections.Counter`** ($O(N)$)。
* **In-place Sort (原地排序)**: `list.sort()` 会永久修改原列表顺序。
* **Side Effects (副作用)**: 函数不应该偷偷修改传入的数据。如果只是为了展示排序结果，使用 `sorted(list)` 创建新副本。

## 2. 💣 踩坑记录 (Error Log)
* **错误现象**: 虽然代码能跑，但修改了全局的 `countries_data` 顺序。
* **原因分析**: 使用了 `lis.sort()`，它是直接在原对象上操作的。
* **解决方案**: 改用 `sorted(lis)`，它会返回一个新的排好序的列表，原数据不动。

## 3. 💅 代码进化 (Before vs After)

**统计语言数量 (Before - 慢):**
```python
# 每次 count 都要重新扫一遍全表
for i in range(len(unique_langs)):
    count = all_langs.count(unique_langs[i])
from collections import Counter
# 一次扫描，瞬间完成
counts = Counter(all_langs).most_common(10)
```