import slabs as sl
import datetime

def calculate_tax_monthly(amount):
    amount = amount * 12
    return calculate_tax_annually(amount) / 12

'''def pre_calculation(func):
    def inner(amount):
        if amount in range(sl.slab1[0],sl.slab1[1]):
            taxableAmount = amount - 1200000
            tax = taxableAmount * 0.125
            tax = tax + 15000
        
            return func()

@pre_calculation
def fetch_tax(amount):
    print(amount)

fetch_tax(499)'''

def calculate_tax_annually(amount):
    tax = 0
    #if amount in range(0, 600000):
    #    return 0
    if amount in range(600000, 1200000):
        taxableAmount = amount - 600000
        tax = taxableAmount * 0.025
        #return tax
    elif amount in range(1200000, 2400000):
        taxableAmount = amount - 1200000
        tax = taxableAmount * 0.125
        tax = tax + 15000
        #return tax
    elif amount in range(2400000, 3600000):
        taxableAmount = amount - 2400000
        tax = taxableAmount * 0.20
        tax = tax + 165000
        #return tax
    elif amount in range(3600000, 6000000):
        taxableAmount = amount - 3600000
        tax = taxableAmount * 0.25
        tax = tax + 405000
        #return tax
    elif amount in range(6000000, 12000000):
        taxableAmount = amount - 6000000
        tax = taxableAmount * 0.325
        tax = tax + 1005000
        #return tax
    else:
        taxableAmount = amount - 12000000
        tax = taxableAmount * 0.35
        tax = tax + 2955000
        #return tax
    return tax


def taxCalculations():
    print("Enter 'm' for monthly tax calculation")
    print("Enter 'a' for annual tax calculation")
    period = input()[0]
    if period == 'm' or period == 'M':
        amount = int(input("Enter your monthly salary in PKR: "))
        tax = calculate_tax_monthly(amount)
        print('*'*10)
        print(f'Monthly Income: {amount}')
        print(f'Monthly Tax: {tax}')
        print(f'Monthly Income after deduction: {amount - tax}')
        print()
        print(f'Annual Income: {amount * 12}')
        print(f'Annual Tax: {tax * 12}')
        print(f'Annual Income after deduction: {(amount - tax) * 12}')

    if period == 'a' or period == 'A':
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

    if period == 'm' or period == 'M':
        return amount,tax
    return amount//12,tax//12

def save_tax_in_file(salary, tax):
    date_obj = datetime.date.today()
    file1 = open(f'{date_obj}.txt','a')
    file1.write(f'Monthly Income: {salary}\n')
    file1.write(f'Tax: {tax}\n')
    file1.write(f'Income after Deduction: {salary - tax}\n\n')
    
    file1.write(f'Annual Income: {salary*12}\n')
    file1.write(f'Tax: {tax*12}\n')
    file1.write(f'Income after Deduction: {(salary - tax)*12}\n\n')
