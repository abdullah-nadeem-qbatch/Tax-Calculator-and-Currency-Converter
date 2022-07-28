from currency_converter import Converter
from history import fetch_history
import tax_calculator as tc
from budget import Budget


print('**** Welcome ****')
print('Enter 1 for Tax Calculation')
print('Enter 2 for Currency Convergence')
print('Enter 3 for Budget Managing')
print('Enter 4 for History')
print('Enter any other key to Exit')
choice = input()[0]

#print(choice)

if choice == '1':
    salary, tax = tc.taxCalculations()
    print("Do you want to save this in txt file? (y/n): ")
    flag = input()[0]
    if flag == 'y' or flag == 'Y':
        tc.save_tax_in_file(salary, tax)

if choice == '2':
    curr = ['USD', 'PKR', 'EURO', 'AUD', 'UAE', 'RIYAL']
    print("\nSelect currency by entering corresponding number: ")
    for (i, item) in enumerate(curr, start = 1):
        print(i, item)
    choice = int(input())
    amount = int(input('Enter amount in ' + curr[choice-1] + ': '))
    c1 = Converter(curr[choice-1], amount)
    c1.convert()
    
if choice == '3':
    bg = Budget()
    bg.getValues()
    bg.saveInFile()


if choice == '4':
    fetch_history()

