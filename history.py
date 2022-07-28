import os

def fetch_history():
    file_name = get_file_name()
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        if file_name in files:
            #print(file_name)
            f = open(str(file_name),'r')
            print(f.read())
            

def get_file_name():
    print("Press 't' to see taxes: ")
    print("Press 'b' to see budgets")
    choice = input()[0]
    if choice == 't':
        print("Enter data:")
        print("Enter date in 'dd' format: ")
        dd = input()
        print("Enter month in 'mm' format: ")
        mm = input()
        print("Enter year in 'yyyy' format: ")
        yyyy = input()
        file_name = yyyy + '-' + mm + '-' + dd + '.txt'
        return file_name
    else:
        print("Enter name")
        name = input()
        file_name = name + '.txt'
        return file_name
