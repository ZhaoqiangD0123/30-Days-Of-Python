# 声明一个空列表
a = list()
b = []

print(a, b)
# 声明一个包含 5 个以上项的列表
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # list of vegetables
print(vegetables)
# 查找列表的长度
print(len(vegetables))
# 获取列表的第一项、中间项和最后一项
mid = len(vegetables) // 2
print(vegetables[0], vegetables[mid], vegetables[-1])
# 声明一个名为 mixed_data_types 的列表，包含你的姓名、年龄、身高、婚姻状况和地址
mixed_data_types = ['DingZhaoqiang', 21, '1.7m', 'no_married', 'Shanxi']
# 声明一个名为 it_companies 的列表，并分配初始值 Facebook、Google、Microsoft、Apple、IBM、Oracle 和 Amazon。
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 使用 print() 打印列表
print(it_companies)
# 打印列表中的公司数
print(f'公司数是{len(it_companies)}')
# 打印第一、中间和最后一家公司
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])
# 修改其中一家公司的名称后打印列表
it_companies[0] = 'Huawei'
print(it_companies)
# 向 it_companies 添加一家 IT 公司
it_companies.append('Xiaomi')
# 在公司列表中间插入一家 IT 公司
it_companies.insert(len(it_companies) // 2, 'Oppo')
print(it_companies)
# 将其中一家 it_companies 公司的名称更改为大写（不包括 IBM!）
it_companies[0] = it_companies[0].upper()
print(it_companies)
# 使用字符串 '#;  ' 连接 it_companies
add = '#;  '
str_companies = add.join(it_companies)
print(str_companies)
# 检查 it_companies 列表中是否存在某个公司。
c = 'ca'
print(f'{c} is in it_companies:{c in it_companies}')
# 使用 sort() 方法对列表进行排序
it_companies.sort()
print(it_companies)
# 使用 reverse() 方法按降序反转列表
it_companies.sort(reverse=True)
print(it_companies)
# 从列表中切分出前 3 家公司
Three_companies = it_companies[0:3]
print(Three_companies)  ##['Xiaomi', 'Oracle', 'Oppo', 'Microsoft', 'IBM', 'HUAWEI', 'Google', 'Apple', 'Amazon']
# 从列表中切分出最后 3 家公司
# last_companies = it_companies[-1:-4:-1]#['Amazon', 'Apple', 'Google']
last_companies = it_companies[-3:]  # ['Google', 'Apple', 'Amazon']
print(last_companies)
# 从列表中切分出中间的 IT 公司或公司
mid_companies = it_companies[len(it_companies) // 2]
print(mid_companies)
# 从列表中删除第一家 IT 公司
it_companies.pop(0)
print(it_companies)
# 从列表中删除中间的 IT 公司或公司
it_companies.pop(len(it_companies) // 2)
# 从列表中删除最后一家 IT 公司
it_companies.pop(-1)
print(it_companies)
# 从列表中删除所有 IT 公司
it_companies.clear()
print(it_companies)
# 销毁 it_companies 列表
del it_companies
# print(it_companies)
# 连接以下列表：

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
con = front_end + back_end
print(con)
# 在连接的列表中插入 Python 和 SQL 到变量 front_end 之后。
l = ['Python', 'SQL']
index = len(front_end)
con[index:index] = l
print(con)

# 以下是 10 个学生的年龄列表：
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# 对列表进行排序，并找出最大和最小年龄
ages.sort()
print(f"最大年龄是{ages[-1]}，最小年龄是{ages[0]}")
# 将最小年龄和最大年龄再次添加到列表中
ages[0:0] = [ages[-1],ages[0]]
ages.sort()
print(ages)
# 找到年龄中位数（一个中间项或两个中间项除以二）
if len(ages)%2 == 0:
    print(f"年龄中位数是{(ages[len(ages)//2]+ages[(len(ages)//2)+1])/2}")
else:
    print(f"年龄中位数是{ages[len(ages)//2]}")
# 找到平均年龄（所有项的总和除以它们的数量）
print(f"平均年龄是{sum(ages)/len(ages)}")
# 找到年龄范围（最大减去最小）
print(f"年龄范围{ages[-1]-ages[0]}")
# 比较 (min - average) 和 (max - average) 的值，使用 abs() 方法
# 在 国家列表 中查找中间的国家
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
# 将国家列表分成两个相等的列表（如果是偶数，如果不是，则第一个半多一个国家）
if len(countries)%2==0:
    country1 = countries[0:len(countries)//2]
    country2 = countries[len(countries)//2:]
else:
    country1 = countries[0:len(countries)//2+1]
    country2 = countries[len(countries)//2+1:]
print(country1[-2:],country2[0:2])
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']。拆解前三个国家和剩下的北欧国家。
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_3 = country[0:3]
country_E = country[3:]
print(country_3)
print(country_E)
