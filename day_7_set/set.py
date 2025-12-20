# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 找到集合 it_companies 的长度
print(len(it_companies))
# 向 it_companies 添加'Twitter'
it_companies.add('Twitter')
print(it_companies)
# 一次性向集合 it_companies 插入多个 IT 公司
it_companies.update(['Xiaomi', 'Huawei'])
print(it_companies)
# 从集合 it_companies 中移除一家公司
it_companies.discard('Huawei')
print(it_companies)
# 移除和丢弃之间有什么区别
# remove() 方法会抛出错误，因此最好先检查该元素是否存在于集合中。discard() 方法则不会抛出任何错误。
# 合并 A 和 B
A_B = A.union(B)
print(A_B)
# 找到 A 和 B 的交集
Both_A_B = A.intersection(B)
# A 是 B 的子集吗
if A.issubset(B):
    print('A是B的子集')
else:
    print('A不是B的子集')
# A 和 B 是不相交集合吗
if A.isdisjoint(B):
    print('A 和 B 是不相交集合')
else:
    print('A 和 B 有相交')
# 将 A 与 B 合并，反之亦然
# 完善写法
C1 = A.union(B)
C2 = B.union(A)
# 验证它们是否相等
print(C1 == C2) # True
# A 和 B 之间的对称差异是什么
# 意思是 (A\B)∪(B\A)
print(f'A 和 B 之间的对称差异是{A.symmetric_difference(B)}')
# 完全删除集合
del A, B

# 将年龄转换为集合并比较列表和集合的长度，哪一个更大？
age_set = set(age)
print(len(age_set))
print(len(age))
# 解释以下数据类型之间的区别：字符串、列表、元组和集合
print('字符串str：\'\' ')
print('列表list：[],有序，可重复，可修改')
print('元组tuple：（），有序，可重复，但不能修改')
print('集合set:{},无序，不重复')

# 数据类型,符号,有序性,可变性,重复性,核心特点
# List (列表),[],✅ 有序,✅ 可变,✅ 可重复,最常用的“箱子”
# Tuple (元组),(),✅ 有序,❌ 不可变,✅ 可重复,安全、只读的数据
# Set (集合),{},❌ 无序,✅ 可变,❌ 不重复,去重、数学运算 (交并差)
# String (字符串),'',✅ 有序,❌ 不可变,✅ 可重复,字符序列，修改需重新赋值



# 我是一个老师，我喜欢激励和教导人们。 这句句子中用了多少独特的单词？使用 split 方法和集合来获取独特的单词。
tense = 'I am a teacher,and i like to encourage and teach people'
tense = tense.replace(',', ' ')
tense = tense.lower()

word_only = set(tense.split())
print(word_only,'\n',len(word_only))
tense = 'I am a teacher,and i like to encourage and teach people'
