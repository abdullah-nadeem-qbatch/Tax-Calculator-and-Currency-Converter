import os
import datetime

def fetch_history():
    file_name = get_file_name()
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        if file_name in files:
            #print(file_name)
            with open(str(file_name),'r') as f:
                print(f.read())


def get_file_name():
    print("Press 't' to see taxes: ")
    print("Press 'b' to see budgets")
    choice = input()[0]
    if choice == 't':
        #print("Enter date:")
        
        return dateInput()
        '''print("Enter date in 'dd' format: ")
        dd = input()
        if not(dd.isdigit() and len(dd)) == 2:
            return False

        print("Enter month in 'mm' format: ")
        mm = input()
        if not(mm.isdigit() and len(mm) == 2):
            return False
        
        print("Enter year in 'yyyy' format: ")
        yyyy = input()
        if not(yyyy.isdigit() and len(mm) == 4):
            return False
        
        file_name = yyyy + '-' + mm + '-' + dd + '.txt'
        return file_name, True'''
    else:
        print("Enter name: ")
        name = input()
        file_name = name + '.txt'
        return file_name, True


def dateInput():
    inputDate = input("Enter the date in format 'dd/mm/yyyy' : ")

    day, month, year = inputDate.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        date = str(year)+'-'+str(month)+'-'+str(day)+'.txt'
        return date
        #print("Input date is valid ..")
    else:
        print("Input date is not valid..")
        dateInput()
