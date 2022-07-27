from dataclasses import dataclass
from currency_converter import Converter
import tax_calculator as tc
import datetime

def taxCalculations():
    print("Enter 'm' for monthly tax calculation")
    print("Enter 'a' for annual tax calculation")
    period = input()[0]
    if period == 'm':
        amount = int(input("Enter your monthly salary in PKR: "))
        tax = tc.calculate_tax_monthly(amount)
        print('*'*10)
        print(f'Monthly Income: {amount}')
        print(f'Monthly Tax: {tax}')
        print(f'Monthly Income after deduction: {amount - tax}')
        print()
        print(f'Annual Income: {amount * 12}')
        print(f'Annual Tax: {tax * 12}')
        print(f'Annual Income after deduction: {(amount - tax) * 12}')

    if period == 'a':
        amount = int(input("Enter your annual salary in PKR: "))
        tax = tc.calculate_tax_annually(amount)
        print('*'*10)
        print(f'Monthly Income: {amount//12}')
        print(f'Monthly Tax: {tax//12}')
        print(f'Monthly Income after deduction: {(amount - tax)//12}')
        print()
        print(f'Annual Income: {amount}')
        print(f'Annual Tax: {tax}')
        print(f'Annual Income after deduction: {amount - tax}')

    if period == 'm':
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

    

print('**** Welcome ****')
print('Enter 1 for Tax Calculation')
print('Enter 2 for Currency Convergence')
print('Enter 3 for Budget Managing')
print('Enter any other key to Exit')
choice = input()[0]

#print(choice)

if choice == '1':
    salary, tax = taxCalculations()
    print("Do you want to save this in txt file? (y/n): ")
    flag = input()[0]
    if flag == 'y' or flag == 'Y':
        save_tax_in_file(salary, tax)

if choice == '2':
    curr = ['USD', 'PKR', 'EURO', 'AUD', 'UAE', 'RIYAL']
    #print("Enter a number from given list: ")
    for (i, item) in enumerate(curr, start = 1):
        print(i, item)
    choice = int(input("Select currency by entering corresponding number: "))
    amount = int(input('Enter amount in ' + curr[choice-1] + ': '))
    c1 = Converter(curr[choice-1], amount)
    c1.convert()
    
if choice == '3':
    pass



