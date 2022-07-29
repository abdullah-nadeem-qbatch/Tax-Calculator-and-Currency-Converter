import slabs as sl
import datetime

def calculate_tax_monthly(amount):
    amount = amount * 12
    return calculate_tax_annually(amount) / 12

def calculate_slab(func):
    def inner(amount, limit, percentage = 1, extra = 0):
        tax = 0
        taxableAmount = amount - limit
        tax = taxableAmount * percentage
        tax = tax + extra
        tax = func(tax)
        return tax
    return inner


@calculate_slab
def tax_calculate(tax_amount):
    return tax_amount


def calculate_tax_annually(amount):
    tax = 0
    if amount < sl.tax_slab['slab1'][0]:
        return tax

    if amount > sl.tax_slab['slab1'][0] and amount <= sl.tax_slab['slab2'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab1'][0], sl.tax_slab['slab1'][1])

    if amount > sl.tax_slab['slab2'][0] and amount <= sl.tax_slab['slab3'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab2'][0], sl.tax_slab['slab2'][1], sl.tax_slab['slab2'][2])

    if amount > sl.tax_slab['slab3'][0] and amount <= sl.tax_slab['slab4'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab3'][0], sl.tax_slab['slab3'][1], sl.tax_slab['slab3'][2])

    if amount > sl.tax_slab['slab4'][0] and amount <= sl.tax_slab['slab5'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab4'][0], sl.tax_slab['slab4'][1], sl.tax_slab['slab4'][2])

    if amount > sl.tax_slab['slab5'][0] and amount <= sl.tax_slab['slab6'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab5'][0], sl.tax_slab['slab5'][1], sl.tax_slab['slab5'][2])

    if amount > sl.tax_slab['slab6'][0]:
        tax = tax_calculate(amount, sl.tax_slab['slab6'][0], sl.tax_slab['slab6'][1], sl.tax_slab['slab6'][2])

    return tax


def taxCalculations():
    print("Enter 'm' for monthly tax calculation")
    print("Enter 'a' for annual tax calculation")
    try:
        period = input()[0]
        if period not in ['m','M','a','A']:
            raise Exception 
    except Exception as e:
        print("Please enter valid character!")
        taxCalculations()

    if any([period == 'm', period == 'M']): #ANY and ALL instead of or and 
        amount = int(input("Enter your monthly salary in PKR: "))
        tax = calculate_tax_monthly(amount)
        print('*' * 10)
        print(f'Monthly Income: {amount}')
        print(f'Monthly Tax: {tax}')
        print(f'Monthly Income after deduction: {amount - tax}')
        print()
        print(f'Annual Income: {amount * 12}')
        print(f'Annual Tax: {tax * 12}')
        print(f'Annual Income after deduction: {(amount - tax) * 12}')

    if any([period == 'a', period == 'A']): #any and all
        amount = int(input("Enter your annual salary in PKR: "))
        tax = calculate_tax_annually(amount)
        print('*'*10)
        print(f'Monthly Income: {amount//12}')
        print(f'Monthly Tax: {tax//12}')
        print(f'Monthly Income after deduction: {(amount - tax)//12}')
        print()
        print(f'Annual Income: {amount}')
        print(f'Annual Tax: {tax}')
        print(f'Annual Income after deduction: {amount - tax}')

    if any([period == 'm', period == 'M']):
        return amount, tax
    return amount // 12, tax // 12


def save_tax_in_file(salary, tax):
    date_obj = datetime.date.today()
    
    with open(f'{date_obj}.txt','a') as file1:
        file1.write("               By Month                               By Year                " + str(datetime.datetime.now()))
        file1.write("\n* ")
        file1.write("- " * 38)
        file1.write("\n|  Salary inc. Tax:  %15d  |  Salary inc Tax:   %15d  |\n" % (salary, salary * 12))
        file1.write("|                                     |                                     |\n")
        file1.write("|  Tax Deduction:    %15d  |  Tax Deduction:    %15d  |\n" % (tax, tax * 12))
        file1.write("|                                     |                                     |\n")
        file1.write("|  Salary after Tax: %15d  |  Salary after Tax: %15d  |\n" % (salary-tax, (salary-tax) * 12))
        file1.write("- " * 39)
        file1.write("\n")
