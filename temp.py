import datetime
salary = 85000
tax = 875

print("\n               By Month                               By Year                " + str(datetime.datetime.now()))
print("* ",end = "")
print("- "*38)
print("|  Salary inc. Tax:  %15d  |  Salary inc Tax:   %15d  |" % (salary, salary * 12))
print("|                                     |                                     |")
print("|  Tax Deduction:    %15d  |  Tax Deduction:    %15d  |" % (tax, tax * 12))
print("|                                     |                                     |")
print("|  Salary after Tax: %15d  |  Salary after Tax: %15d  |" % (salary-tax, (salary-tax) * 12))
print("- "*39)