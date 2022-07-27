import tax_calculator as tc
class Budget:
    def __init__(self, name = "", income = 0, monthlyTax = 0, grocery = 0,
     traveling = 0, medical = 0, entertainment = 0, bills = 0):
        self.name = name
        self.income = income
        self.montlyTax = monthlyTax
        self.grocery = grocery
        self.traveling = traveling
        self.medical = medical
        self.entertainment = entertainment
        self.bills = bills

    def getValues(self):
        self.name = input("Enter your Name: ")
        self.income = input("Enter your Monthly Income: ")
        #self.montlyTax = tc.calculate_tax_monthly(self.income)
        self.grocery = input("Enter your Grocery Expenses: ")
        self.traveling = input("Enter your Traveling Expenses: ")
        self.medical = input("Enter your Medical Expenses: ")
        self.entertainment = input("Enter your Entertainment Expenses: ")
        self.bills = input("Enter your Bills Expenses: ")
    

    def pre_calculation(self, func):
        def inner(func):
            self.montlyTax = tc.calculate_tax_monthly(self.income)
            func()
        return inner


    @pre_calculation
    def saveInFile(self):
        file1 = open(f'{self.name}.txt','a')
        file1.write(f'Name: {self.name}\n')
        file1.write(f'Income: {self.income}\n')
        file1.write(f'Monthly Tax: {self.montlyTax}\n')
        file1.write(f'Grocery: {self.grocery}\n')
        file1.write(f'Traveling: {self.traveling}\n')
        file1.write(f'Entertainment: {self.entertainment}\n')
        file1.write(f'Bills: {self.bills}\n')

b1 = Budget()
b1.getValues()
b1.saveInFile()