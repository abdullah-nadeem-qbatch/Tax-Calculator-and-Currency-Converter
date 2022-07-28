from currency_converter import Converter
from history import fetch_history
import tax_calculator as tc
from budget import Budget
from menu import welcome_menu

def dashboard():

    welcome_menu()
    choice = input()[0]        

    if choice == '1':
        salary, tax = tc.taxCalculations()
        print("Do you want to save this in txt file? (y/n): ")
        flag = input()[0]
        if flag == 'y' or flag == 'Y':
            tc.save_tax_in_file(salary, tax)

    elif choice == '2':
        curr = ['USD', 'PKR', 'EURO', 'AUD', 'UAE', 'RIYAL']
        print("\nSelect currency by entering corresponding number: ")
        for (i, item) in enumerate(curr, start = 1):
            print(i, item)
        choice = int(input())
        amount = int(input('Enter amount in ' + curr[choice-1] + ': '))
        c1 = Converter(curr[choice-1], amount)
        c1.convert()
        
    elif choice == '3':
        bg = Budget()
        bg.getValues()
        bg.saveInFile()

    elif choice == '4':
        fetch_history()

    elif choice == '5':
        return
   
    else:
        print("Please enter a correct choice: \n")
        dashboard()