"""
Made by root
With Love

For Support rootuser on Discord
"""

import json
from os import system
from random import choice, randint

logo = """
  _____                _                        ___  ___                                                  _   
 |  ___|              | |                       |  \/  |                                                 | |  
 | |__ _ __ ___  _ __ | | ___  _   _  ___  ___  | .  . | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
 |  __| '_ ` _ \| '_ \| |/ _ \| | | |/ _ \/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
 | |__| | | | | | |_) | | (_) | |_| |  __/  __/ | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
 \____/_| |_| |_| .__/|_|\___/ \__, |\___|\___| \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                | |             __/ |                                      __/ |                              
                |_|            |___/                                      |___/                               
"""
correct_login_1 = "admin"
correct_password_1 = "admin123"

correct_login_2 = "root"
correct_password_2 = "root123"

inputed_login = ""
inputed_password = ""


with open('./config/config.json', 'r') as config_file:
    config_data = json.load(config_file)
    color = str(config_data['color'])
    
system('cls')
system('color ' + color)

def login():
    system('cls')
    print(logo)
    print()
    print('Employee Management System 1.0.0')
    print()
    
    print('Username:')
    inputed_login = input(' > ')
    
    print('Password:')
    inputed_password = input(' > ')
    authenticate_admin(inputed_login, inputed_password)
        
def authenticate_admin(inputed_login, inputed_password):
        if inputed_login == correct_login_1 or inputed_login == correct_login_2:
            if inputed_password == correct_password_1 or inputed_password == correct_password_2:
                print('Login successful.')
                input('Press Enter to continue.')
                after_login()
            else:
                
                print('Invalid password. Please try again.')
                input('Press Enter to continue.')
                login()
                
        else: 
            print('Invalid login or password. Please try again.')
            input('Press Enter to continue.')
            login()
    
    
def after_login():
    system('cls')
    print(logo)
    print()
    print(' Employee Management System 1.0.0')
    print()
    print(' ╔════════════════════════════════════════╗')
    print(' ║ (1) > Enter Employee Management System ║')
    print(' ║ (2) > About                            ║')
    print(' ║ (3) > Credits                          ║')
    print(' ║ (4) > License                          ║')
    print(' ╠════════════════════════════════════════╣')
    print(' ║ (5) > Logout                           ║')
    print(' ╚════════════════════════════════════════╝')
    
    after_login_choice = int(input('  > '))
    
    if after_login_choice == 1:
        menu()
        
    elif after_login_choice == 2:
        print('Name: Employee Management System')
        print('Version: 1.0.0')
        print('Langauge: Python 3.12')
        print('Made by root')
        
        input()
        after_login()
        
    elif after_login_choice == 3:
        print('Owner - Root')
        print('If you want to add me on Discord my nickname is rootuser')
        
        input()
        after_login()
        
    elif after_login_choice == 4:
        print('GNU GENERAL PUBLIC LICENSE')
        
        input()
        after_login()
        
    elif after_login_choice == 5:
        logout()
    else:
        after_login()

def menu():
    system('cls')
    print(logo)
    print()
    print(' Employee Management System 1.0.0')
    print()
    print(' ╔═════════════════════════════╗')
    print(' ║ (1) > Add Employee          ║')
    print(' ║ (2) > Remove Employee       ║')
    print(' ║ (3) > Edit Employee         ║')
    print(' ║ (4) > List Employees        ║')
    print(' ║ (5) > Show Employee Profile ║')
    print(' ║ (6) > Generate Random Data  ║')
    print(' ╠═════════════════════════════╣')
    print(' ║ (7) > Go Back               ║')
    print(' ║ (8) > Logout                ║')
    print(' ╚═════════════════════════════╝')
    
    choice = int(input('  > '))

    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_employee()
    elif choice == 3:
        edit_employee()
    elif choice == 4:
        list_employees()
    elif choice == 5:
        show_employee_profile()
    elif choice == 6:
        generate_random_data()
    elif choice == 7:
        go_back()
    elif choice == 8:
        logout()
    else:
        system('cls')
        print('Invalid Choice')
        menu()

def add_employee():
    system('cls')
    print(' ╔═══════════════╗')
    print(' ║ Add Employee: ║')
    print(' ╚═══════════════╝')
    print('')
    employee_id = int(input('Employee ID: '))
    employee_name = input('Employee First Name: ')
    employee_surname = input('Employee Last Name: ')
    employee_age = int(input('Employee Age: '))
    employee_gender = input('Employee Gender: ')
    employee_role = input('Employee Role: ')
    employee_password = ''
    print('')

    employee_data = {
        'ID': employee_id,
        'First Name': employee_name,
        'Last Name': employee_surname,
        'Age': employee_age,
        'Gender': employee_gender,
        'Role': employee_role,
        'Password': employee_password
    }

    confirm = input('Do you want to add this employee? (Yes/No): ')
    if confirm.lower() == 'yes':
        with open('employees.json', mode='a') as file:
            json.dump(employee_data, file)
            file.write('\n')
    

        system('cls')
        print('Adding Employee')
        print('Employee ID:', employee_id)
        print('Employee First Name:', employee_name)
        print('Employee Last Name:', employee_surname)
        print('Employee Age:', employee_age)
        print('Employee Gender:', employee_gender)
        print('Employee Role:', employee_role)
        
        print('')
        input('Press Enter key to add.')
    else:
        print('Addition canceled.')

    menu()

def remove_employee():
    system('cls')
    print(' ╔══════════════════╗')
    print(' ║ Remove Employee: ║')
    print(' ╚══════════════════╝')
    print()
    
    employee_id = int(input('Enter Employee ID to remove: '))

    employees = []

    with open('employees.json', mode='r') as file:
        for line in file:
            employee = json.loads(line)
            if employee['ID'] == employee_id:
                print('Employee Found:')
                print('Employee ID:', employee['ID'])
                print('Employee First Name:', employee['First Name'])
                print('Employee Last Name:', employee['Last Name'])
                print('Employee Age:', employee['Age'])
                print('Employee Gender:', employee['Gender'])
                print('Employee Role:', employee['Role'])
                print('')
                
                confirm = input('Do you want to remove this employee? (Yes/No): ')
                
                if confirm.lower() == 'yes':
                    print('Employee removed successfully.')
                else:
                    print('Removal canceled.')
            else:
                employees.append(employee)

    with open('employees.json', mode='w') as file:
        for employee in employees:
            json.dump(employee, file)
            file.write('\n')

    print('Press Enter key to continue.')
    input()
    menu()

def edit_employee():
    system('cls')
    print(' ╔════════════════╗')
    print(' ║ Edit Employee: ║')
    print(' ╚════════════════╝')
    print()
    
    employee_id = int(input('Enter Employee ID to edit: '))

    employees = []

    with open('employees.json', mode='r') as file:
        for line in file:
            employee = json.loads(line)
            if employee['ID'] == employee_id:
                print('Employee Found:')
                print('Employee ID:', employee['ID'])
                print('Employee First Name:', employee['First Name'])
                print('Employee Last Name:', employee['Last Name'])
                print('Employee Age:', employee['Age'])
                print('Employee Gender:', employee['Gender'])
                print('Employee Role:', employee['Role'])
                print('')
                print('Enter new details:')
                
                employee['First Name'] = input('Employee First Name: ')
                employee['Last Name'] = input('Employee Last Name: ')
                employee['Age'] = int(input('Employee Age: '))
                employee['Gender'] = input('Employee Gender: ')
                employee['Role'] = input('Employee Role: ')
                
                print('')
                confirm = input('Do you want to save these changes? (Yes/No): ')
                if confirm.lower() == 'yes':
                    print('Employee details updated successfully.')
                else:
                    print('Changes canceled.')
                    
            employees.append(employee)

    with open('employees.json', mode='w') as file:
        for employee in employees:
            json.dump(employee, file)
            file.write('\n')
            
    print('Press Enter key to continue.')
    input()
    menu()

def list_employees():
    system('cls')
    print(' ╔═════════════════╗')
    print(' ║ List Employees: ║')
    print(' ╚═════════════════╝')
    print('')

    with open('employees.json', mode='r') as file:
        for line in file:
            employee = json.loads(line)
            print('Employee ID:', employee['ID'])
            print('Employee First Name:', employee['First Name'])
            print('Employee Last Name:', employee['Last Name'])
            print('Employee Age:', employee['Age'])
            print('Employee Gender:', employee['Gender'])
            print('Employee Role:', employee['Role'])
            
            print('')

    print('Press Enter key to continue.')
    input()
    menu()
    
def show_employee_profile():
    system('cls')
    print(' ╔════════════════╗')
    print(' ║ Show Employee: ║')
    print(' ╚════════════════╝')
    print()
    employee_id = int(input('Enter Employee ID to show: '))

    with open('employees.json', mode='r') as file:
        for line in file:
            employee = json.loads(line)
            if employee['ID'] == employee_id:
                print('Employee Found:')
                print('Employee ID:', employee['ID'])
                print('Employee First Name:', employee['First Name'])
                print('Employee Last Name:', employee['Last Name'])
                print('Employee Age:', employee['Age'])
                print('Employee Gender:', employee['Gender'])
                print('Employee Role:', employee['Role'])
                
                print('')
                
    print('Press Enter key to continue.')
    input()
    menu()

def generate_random_data():
    print(' ╔══════════════════╗')
    print(' ║ Random Employee: ║')
    print(' ╚══════════════════╝')
    
    print()
    print(f"ID: {randint(1, 100)}")
    print(f"First Name: {choice(['John', 'Emma', 'Michael', 'Sarah', 'Daniel', 'Olivia', 'James', 'Emily', 'David', 'Sophia', 'William', 'Isabella', 'Liam', 'Mia', 'Benjamin', 'Charlotte', 'Jacob', 'Amelia', 'Ethan', 'Harper'])}")
    print(f"Last Name: {choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Davis', 'Miller', 'Wilson', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Robinson', 'Clark', 'Lewis'])}")
    print(f"Age: {randint(18, 62)}")
    print(f"Gender: {choice(['Male', 'Female'])}")
    print(f"Role: {choice(['Owner', 'CoOwner', 'Senior Developer', 'System Architect', 'Database Administrator', 'Junior Developer', 'Developer', 'Tester', 'Network Administrator', 'Business Analyst', 'Technical Support Specialist', 'Intern'])}")
    
    print()
    print('Press Enter key to continue.')
    input()
    menu()

def go_back():
    after_login()
    
def logout():
    login()
    
login()
