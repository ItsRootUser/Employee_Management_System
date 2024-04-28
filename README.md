# Employee Management System

This is a simple command-line based Employee Management System written in Python. It allows you to manage a list of employees, add new employees, remove existing employees, edit employee details, list all employees and view employee details.

## Requierments

- Python 3.12 or higher

## Getting Started

1. Download the release `main.zip`.
2. If you want to erase every dummy data employy erase the content of `./employees.json`
3. Run the script using the command `python "main.py"` in your terminal or command prompt.

## Login

Upon starting the script, you will be presented with a login screen. Default login is `admin` and password is `admin123`.

## After Login

After successful login, you will be presented with a main menu which has the following options:

- Enter Employee Management System
- About
- Credits
- Licence
- Logout

## Employee Management System

Selecting option 1 will take you to the Employee Management System menu which has the following options:

- Add Employee
- Remove Employee
- Edit Employee
- List Employees
- Show Employee Profile
- Logout

## Add Employee

Selecting option 1 will allow you to add a new employee. You will be asked to enter the following details:

- Employee ID
- Employee First Name
- Employee Last Name
- Employee Age
- Employee Gender
- Employee Role

## Remove Employee

Selecting option 2 will allow you to remove an existing employee. You will be asked to enter the Employee ID of the employee you want to remove.

## Edit Employee

Selecting option 3 will allow you to edit the details of an existing employee. You will be asked to enter the Employee ID of the employee you want to edit. After entering the Employee ID, you will be asked to enter the new details for the employee.

## List Employees

Selecting option 4 will display the details of all employees in the `employees.json` file.

## Show Employee Profile

Selecting option 5 will display the details of the employee with the entered Employee ID.

## Logout

Selecting option 6 will log you out of the system and take you back to the login screen.

## Note

The `employees.json` file is used to store the details of all employees. The details are stored in JSON format. The script will automatically create the `employees.json` file if it does not exist.

## About

This Employee Management System was created as a simple project to demonstrate the use of Python for command-line based applications.

## Credits

This Employee Management System was created by root.

## Licence

This Employee Management System is released under the GNU GENERAL PUBLIC LICENSE.