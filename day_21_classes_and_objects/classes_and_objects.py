# 创建一个名为PersonAccount的类。它有firstname、lastname、incomes、expenses属性和添加收入、添加支出以及账户余额方法。
class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expense):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expense = expense

    def add_incomes(self, income):
        self.incomes += income
        print(self.incomes)

    def add_expense(self, expense):
        self.expense += expense
        print(self.expense)
    def info_Person(self):
        print(f'{self.firstname} {self.lastname},income:{self.incomes},expense:{self.expense}')


class net_asset(PersonAccount):
    def __init__(self,firstname, lastname, incomes, expense,net_asset = 0):
        super().__init__(firstname, lastname, incomes, expense)
        self.net_asset = 0

    def count_asset(self):
        self.net_asset = self.incomes-self.expense
        print(self.net_asset)



A1 = PersonAccount('Wang', 'Xiaoming', 20000, 12000)
A1.info_Person()
A1.add_expense(200)
A1.add_incomes(500)
A1.info_Person()

A2 = net_asset('Wang', 'Xiaoming', 20000, 12000)
A2.info_Person()
A2.count_asset()

class print_product:
    def print_products(*args, **kwargs):
        for product in args:
            print(product)
        print(kwargs)
        for key in kwargs:
            print(f"{key}: {kwargs[key]}")

B1 = print_product
B1.print_products("apple", "banana", "orange", vegetable="tomato", juice="orange")

