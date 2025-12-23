# 声明一个函数 add_two_numbers。它接受两个参数并返回它们的和。
def add_two_numbers(number1, number2):
    return number1 + number2


print(add_two_numbers(number2=6, number1=3))


# 圆的面积计算公式为：area = π x r x r。编写一个函数计算 area_of_circle。
def area_of_circle(r):
    pai = 3.14
    return r * r * pai


x = 10
print(f'半径为{x}的圆面积是{area_of_circle(x)}')


# 编写一个名为 add_all_nums 的函数，它接受不定数量的参数并求和所有参数。检查所有列表项是否都是数字类型。如果不是，给予合理的反馈。
def add_all_nums(*nums):
    total_num = 0
    for i in nums:
        try:
            total_num += i
        except:
            print(f'{i}不是数字')
            return '无法求和'
    return total_num


# 编写一个名为 calculate_slope 的函数，它返回线性方程的斜率。
def calculate_slope(a=0, b=0, c=0):  # Ax + By + C = 0
    k = -(a / b)
    print(f'方程{a}x + {b}y + {c} = 0的斜率是{k}')
    return k


calculate_slope(2, -1, 3)


# 二次方程按以下公式计算：ax² + bx + c = 0。编写一个函数计算二次方程的解集，solve_quadratic_eqn。
def solve_quadratic_eqn(a=0, b=0, c=0):
    solve = []
    delta = b * b - 4 * a * c
    print(delta)
    if delta >= 0:
        solve.append((-b + delta ** (1 / 2)) / (2 * a))
        solve.append((-b - delta ** (1 / 2)) / (2 * a))
        print(solve)
    else:
        print('没有解')
    return solve


solve_quadratic_eqn(1, -5, 6)


# 声明一个名为add_item的函数。它接受一个列表和一个项作为参数。它返回在末尾添加项的列表。
def add_item(lis: list, item) -> list:
    c = lis.append(item)
    return lis


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# 声明一个名为 capitalize_list_items 的函数。它接受一个列表作为参数，并返回一个大写的列表项。
def capitalize_list_items(lis:list):
    lis_caps = [word.upper() for word in lis ]
    return lis_caps
print(capitalize_list_items(['adfsa','Adfds']))


# 编写一个函数检查列表中的所有项是否都是唯一的。
def is_only_list(lis:list):
    lis_st = set(lis)
    if len(lis_st) == len(lis):
        print('是唯一的')
    else:
        print('不是唯一的')

is_only_list(['ii','adfa','iid',12])


# 编写一个函数检查列表中的所有项是否都是相同的数据类型。
def is_only_type_list(lis: list):
    # lis.sort(key=lambda x: str(type(x)))#会修改原列表顺序 (副作用)，排序的时间复杂度是 O(N log N)，这比直接检查 O(N) 要慢
    # if str(type(lis[0])) == str(type(lis[-1])):
    #     print('都是相同的数据类型')
    # else:
    #     print('不都是相同的数据类型')
    if not lis: return True  # 空列表默认一致

    first_type = type(lis[0])
    # 翻译：对于 lis 里的每一个 item，检查它的类型是否等于 first_type
    # all() 函数：只有全为 True 才返回 True
    result = all(type(item) == first_type for item in lis)

    if result:
        print('都是相同的数据类型')
    else:
        print('不都是相同的数据类型')
    return result


is_only_type_list(['adfsa','adfas','45'])