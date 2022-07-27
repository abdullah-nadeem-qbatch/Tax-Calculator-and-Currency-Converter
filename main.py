from currency_converter import Converter
import tax_calculator as tc

print('**** Welcome ****')
print('Enter 1 for Tax Calculation')
print('Enter 2 for Currency Convergence')
print('Enter 3 for Budget Managing')
print('Enter any other key to Exit')
choice = input()[0]

#print(choice)

if choice == '1':
    print("Enter m for monthly tax calculation")
    print("Enter a for annual tax calculation")
    period = input()[0]
    if period == 'm':
        amount = int(input("Enter your monthly salary in PKR: "))
        print("Tax: " + str(tc.calculate_tax_monthly(amount)))
    if period == 'a':
        amount = int(input("Enter your annual salary in PKR: "))
        print("Tax: " + str(tc.calculate_tax_annually(amount)))

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