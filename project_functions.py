""""
Group Project
Modules used in the project
Author: Kamala Ramesh (700745451)
"""

import re

def read_file(file_name):
    # Function to read file
    with open(file_name, 'r', encoding='utf8' ) as f:
        return f.read()

def check_password(pwd):
    # Function to check password
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
    if (pwd[0] not in symbols):
        return False
    elif not (6 <= len(pwd) <= 12):
        return False
    elif not (re.search(r'[A-Z]', pwd) and
        re.search(r'[a-z]', pwd) and
        re.search(r'\d', pwd)
        ):
        return False
    else:
        return True


def username_check(user_name):
    # Function to check the username
    condition1 = len(user_name) <= 6 and len(user_name) >= 3
    condition2 = user_name[0].isupper()
    if condition1 and condition2:
        return True
    else:
        return False

def name_check(name):
    # Function to check the name
    name = name.split(' ')
    condition1 = name[0][0].isupper() and name[1][0].isupper()
    condition2 = len(name[0]) >= 2 and len(name[1]) >= 2
    condition3 = not any(char.isdigit() for char in name[0] + name[1])

    # Check all conditions using an if statement
    if condition1 and condition2 and condition3:
        return True
    else:
        return False

def age_check(age):
    # Function to check age
    if (0 <= int(age) <= 100):
        return True
    else:
        return False

def gender_check(gender):
    # Function to check gender
    if gender.upper() in ['M', 'F', 'O']:
        return True
    else:
        return False

def phone_check(phone):
    # Function to check phone number
    phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    condition = bool(re.match(phone_pattern, phone))
    if condition:
        return True
    else:
        return False


def exit_system():
    # function to exit the system
    exit_check = input('Do you want to Exit the System? Enter Y to confirm: ')
    if exit_check.upper() == 'Y':
        print('Exit the system...')
        exit()

