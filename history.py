import os
import datetime

def fetch_history():
    '''
    Displays history/content of searched file 
    '''
    file_name = get_file_name()
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        if file_name in files:
            #print(file_name)
            with open(str(file_name),'r') as f:
                print(f.read())


def get_file_name():
    '''
    This functions gets the validated file name from user
    '''
    print("Press 't' to see taxes: ")
    print("Press 'b' to see budgets")
    choice = input()[0]
    
    if choice == 't':        
        return dateInput()
     
    else:
        print("Enter name: ")
        name = input()
        file_name = name + '.txt'
        return file_name, True


def dateInput():
    '''
    Inputs date in correct format which can be further searched
    '''
    inputDate = input("Enter the date in format 'dd/mm/yyyy' : ")

    day, month, year = inputDate.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if isValidDate:
        date = str(year) + '-' + str(month) + '-' + str(day) + '.txt'
        return date
        #print("Input date is valid ..")
    else:
        print("Input date is not valid..\n")
        dateInput()
