import json
from os import system

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

system('cls')
system('color 0A')

def login_menu():
    system('cls')
    print(logo)
    print()
    print(' ╔════════════╗')
    print(' ║ (1) Login  ║')
    print(' ║ (2) Signin ║')
    print(' ╚════════════╝')
    print()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        login()
    if choice == '2':
        signin()
    else:
        login_menu()

def login():
    system('cls')
    print(logo)
    print()
    print("Welcome Employee")
    print("Please Login:")
    print("")
    print("ID:")
    user_id = input(" > ")
    print("Password:")
    user_password = input(" > ")

    if authenticate_user(user_id, user_password) == True:
        menu()
    else:
        login()
        
def signin():
    system('cls')
    print(logo)
    print()
    print(' ╔═════════╗')
    print(' ║ Sign in ║')
    print(' ╚═════════╝')
    print()
    print('To create account, please contact the system administrator.')
    print()
    input('Press Enter key to continue.')
    menu()
    

def authenticate_user(user_id, user_password):
    with open('employees.json', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if  int(user_id) == user_data.get('ID') and (user_password) == user_data.get('Password'):
                user_name = user_data.get('First Name') + ' ' + user_data.get('Last Name')
                global ID
                global Name
                ID = user_id
                Name = user_name
                return True
    return False

def menu():
    system('cls')
    print(logo)
    print()
    print("Logged in as " + Name + ".")
    print()
    print(' ╔══════════════════╗')
    print(' ║ (1) View Profile ║')
    print(' ╠══════════════════╣')
    print(' ║ (2) Logout       ║')
    print(' ╚══════════════════╝')
    print()
    choice = input("Enter your choice: ")

    if choice == '1':
        view_profile()
    elif choice == '2':
        print("Logged out successfully.")
        login()
    else:
        print("Invalid choice. Please try again.")
        menu()

def view_profile():
    system('cls')

    print(' ╔═══════════════╗')
    print(' ║ Show Profile: ║')
    print(' ╚═══════════════╝')
    print()
    
    with open('employees.json', mode='r') as file:
        for line in file:
            employee = json.loads(line)
            if employee['ID'] == int(ID):
                print('Employee Found:')
                print('Employee ID:', employee['ID'])
                print('Employee First Name:', employee['First Name'])
                print('Employee Last Name:', employee['Last Name'])
                print('Employee Age:', employee['Age'])
                print('Employee Gender:', employee['Gender'])
                print('Employee Role:', employee['Role'])
                print('')
                
    input('Press Enter key to continue.')
    menu()

login()
