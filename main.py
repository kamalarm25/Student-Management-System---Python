""""
Group Project
Main Page
Author: Kamala Ramesh (700745451)
"""

import user_registration as user
import student_records as student
import student_scores as score
import hashlib

from tabulate import tabulate
from sqlalchemy.orm import sessionmaker
from user_registration import User
from student_records import Student
from student_scores import Score
from sqlalchemy import select, update, delete
from project_functions import *


# Create a session to interact with the database
c_engine = user.create_db()
c_session = sessionmaker(bind=c_engine)()

s_engine = student.create_db()
s_session = sessionmaker(bind=s_engine)()

sc_engine = score.create_db()
sc_session = sessionmaker(bind=sc_engine)()

def login():
    print('=' * 24 + 'Login' + '=' * 24)

    # Validate if the account name exists
    while True:
        account_name = input('Please enter your Account: ')
        result_acc = c_session.execute(select(User).where(User.userid == account_name)).scalars().all()
        if len(result_acc) == 0:
            print('\t \u274c Login failed! Account does not exist')
        else:
            break

    # Validate if the password matches the account's password
    while True:
        password = input('Please enter your Password: ')
        hashed_pwd = hashlib.md5(password.encode())
        if str(result_acc[0].password) != hashed_pwd.hexdigest():
            print('\t \u274c Login failed! Incorrect Password')
        else:
            break

    # When both validations as passed open Studnet file
    s_content = read_file('student.txt') %(account_name)
    while True:
        s_code = input(s_content + '\nPlease select (1 - 6): ')
        #print(s_code)
        if s_code == '1':
            student1()
        elif s_code == '2':
            student2()
        elif s_code == '3':
            student3()
        elif s_code == '4':
            student4()
        elif s_code == '5':
            student5()
        elif s_code == '6':
            break
        else:
            print('\t \u274c Invalid Code')

def student1():
    # Print the requirements for adding a student
    print('=' * 21 + 'Add Student' + '=' * 21)
    print('\t1. The first letter of firstname and lastname must be capitalized')
    print('\t2. Firstname and lastname must each have at least two letters')
    print('\t3. No digit allowed in the name')
    print('\t4. Age must between 0 and 100')
    print('\t5. Gender can be M (Male), F (Female) or O (Other)')
    print('\t6. Phone must be in the (xxx-xxx-xxxx) format')
    print('\t7. Major must be in CS, CYBR, IT, SE or DSA')

    while True:
        result = list(s_session.execute(select(Student.id).order_by('id')))
        if len(result) == 0:
            id = 700300001
        else:
            id = int(result[-1][0]) + 1

        # Validate the student name
        while True:
            name = input('Please Enter Student\'s Name (Firstname Lastname): ')
            if not name_check(name):
                print('\t \u274C Invalid Student Name')
            else:
                break

        # Validate the student age
        while True:
            age = input('Please Enter Student\'s Age: ')
            if not age_check(age):
                print('\t \u274C Invalid Student Age')
            else:
                break

        # Validate the student gender
        while True:
            gender = input('Please Enter Student\'s Gender: ')
            if not gender_check(gender):
                print('\t \u274C Invalid Student Gender')
            else:
                gender=gender.upper()
                break

        # Validate the student major
        while True:
            major = input('Please Enter Student\'s Major: ')
            if major.upper() in ['CS', 'CYBR', 'IT', 'SE', 'DSA']:
                break
            else:
                print('\t \u274C Invalid Major')

        # Validate the student phone numebr
        while True:
            phone = input('Please Enter Student\'s Phone: ')
            if not phone_check(phone):
                print('\t \u274C Invalid Student Phone Number')
            else:
                break

        try:
            # When all validations are passed create the student record
            s = Student(id=str(id), name=name, age=age, gender=gender, major=major, phone=phone)
            s_session.add(s)
            s_session.commit()

            # Simultaneously create a score record for the student with default score as zero
            sc = Score(id=str(id), name=name, CS1030=0, CS1100=0, CS2030=0)
            sc_session.add(sc)
            sc_session.commit()

            print('\t \u2714 Student Added Successfully')
            print('\t \u2666 1. Continue')
            print('\t \u2666 2. Exit')

        except Exception as e:
            s_session.rollback()
            sc_session.rollback()
            print("Error:", e)

        finally:
            s_session.close()
            sc_session.close()
            

        # Check if user needed to add another user else exit
        s1_code = input('Please select 1 or 2: ')
        if s1_code == '1':
            continue
        else:
            break

def student2():
    print('=' * 21 + 'Show Student' + '=' * 21)
    print('\t \u2666 1. Show all Students ')
    print('\t \u2666 2. Show Students by Name')
    print('\t \u2666 3. Show Students by ID')
    print('\t \u2666 Other Return')
    headers = ['ID', 'Name', 'Age', 'Gender', 'Major', '\u260E']
    colalign = ["left", "left", "right", "center", "center", "left"]

    s2_code = input('Please select: ')
    # Display all the Student records
    if (s2_code == '1'):
        result = s_session.execute(select(Student.id, Student.name, Student.age, Student.gender, Student.major, Student.phone))
        rows = result.fetchall()
        if not rows:
            print('\t \u274C No student existing')
            #len(result) == 0
        else:
            print('=' * 30 + 'Student Record' + '=' * 30)
            table = tabulate(rows, headers=headers, tablefmt="plain", colalign=colalign)
            print(table)
            #print('=' * 74)

    # Display student record by name
    elif (s2_code == '2'):
        student_name = input('Please enter Student Name to Display: ')
        result = s_session.execute(select(Student.id, Student.name, Student.age, Student.gender, Student.major, Student.phone).where(Student.name == student_name))
        rows = result.fetchall()
        if not rows:
            print(f'\t \u274C No student exsiting with name, {student_name}')
        else:
            print('=' * 30 + 'Student Record' + '=' * 30)
            table = tabulate(rows, headers=headers, tablefmt="plain", colalign=colalign)
            print(table)
            #print('=' * 74)

    # Display student record by ID
    elif (s2_code == '3'):
        student_id = input('Please enter Student ID to Display: ')
        result = s_session.execute(
            select(Student.id, Student.name, Student.age, Student.gender, Student.major, Student.phone).where(
                Student.id == student_id))
        rows = result.fetchall()
        if not rows:
            print(f'\t \u274C No student exsiting with id, {student_id}')
        else:
            print('=' * 30 + 'Student Record' + '=' * 30)
            table = tabulate(rows, headers=headers, tablefmt="plain", colalign=colalign)
            print(table)
            #print('=' * 74)

    else:
        return

def student3():
    print('=' * 21 + 'Modify Student' + '=' * 21)
    student_id = input('Please enter the Student ID to Modify: ')
    result = s_session.execute(select(Student.id).where(Student.id == student_id)).fetchall()

    # Validate if the record exists for the given student ID
    if not result:
        print('\t \u274C No Record Found')

    else:
        # Update the age of the student
        new_age = input('New age (press enter without modification: ')
        while True:
            if new_age == '':
                break
            elif not age_check(new_age):
                print('\t \u274C Invalid Student Age')
                new_age = input('Please Enter Student Age: ')
            else:
                s_session.execute(update(Student).where(Student.id == student_id).values(age = new_age))
                s_session.commit()
                break

        # Update the major of the Student
        while True:
            new_major = input('New major (press enter without modification: ')
            if new_major == '':
                break
            elif new_major.upper() not in ['CS', 'CYBR', 'IT', 'SE', 'DSA']:
                print('\t \u274C Invalid Major')
            else:
                s_session.execute(update(Student).where(Student.id == student_id).values(major = new_major))
                s_session.commit()
                break

        # Update the phone of the Student
        new_phone = input('New phone (press enter without modification: ')
        while True:
            if new_phone == '':
                break
            elif not phone_check(new_phone):
                print('\t \u274C Invalid Student Phone')
                new_phone = input('Please Enter Student Phone: ')
            else:
                s_session.execute(update(Student).where(Student.id == student_id).values(phone = new_phone))
                s_session.commit()
                break

        if new_age != '' or new_major != '' or new_phone != '':
            print('\t \u2714 Student Modified Successfully')
        else:
            print('No modification made.....')

def student4():
    print('=' * 21 + 'Delete Student' + '=' * 21)
    print('\t \u2666 1. Delete Students by Name')
    print('\t \u2666 2. Delete Students by ID')
    print('\t \u2666 Other Return')

    s4_code = input('Please select: ')


    # Delete students by name
    if (s4_code == '1'):
        student_name = input('Please Enter Student Name to Delete: ')
        result = s_session.execute(delete(Student).where(Student.name == student_name))
        s_session.commit()

        sc_session.execute(delete(Score).where(Score.name == student_name))
        sc_session.commit()

    # Delete student by ID
    elif (s4_code == '2'):
        student_id = input('Please Enter Student ID to Delete: ')
        result = s_session.execute(delete(Student).where(Student.id == student_id))
        s_session.commit()

        sc_session.execute(delete(Score).where(Score.id == student_id))
        sc_session.commit()
    else:
        return

    delete_count = result.rowcount
    if delete_count > 0:
        print('\t \u2714 Record Deleted Successfully')
    else:
        print('\t \u274C No Record Found')

def student5():
    print('=' * 21 + 'Query Student Records' + '=' * 21)
    print('\t \u2666 1. Display Student Score by Name')
    print('\t \u2666 2. Update Student Score by ID')
    print('\t \u2666 Other Return')

    s5_code = input('Please select: ')
    headers = ['ID', 'Name', 'CS1030', 'CS1100', 'CS2030']
    colalign = ["left", "left", "center", "center", "center"]

    # Display Student score using name
    if s5_code == '1':
        student_name = input('Please enter Student Name to Display the Score: ')
        result = sc_session.execute(
            select(Score.id, Score.name, Score.CS1030, Score.CS1100, Score.CS2030).where(
                Score.name == student_name))
        rows = result.fetchall()
        if not rows:
            print(f'\t \u274C No student exsiting with name, {student_name}')
        else:
            print('=' * 30 + 'Student Record' + '=' * 30)
            table = tabulate(rows, headers=headers, tablefmt="plain", colalign=colalign)
            print(table)

    # Update Student score using ID
    elif s5_code == '2':
        student_id = input('Please enter Student ID to update the Score: ')
        new_score1 = input('New grade for CS1030 (press enter without modification): ')
        new_score2 = input('New grade for CS1100 (press enter without modificaiton): ')
        new_score3 = input('New grade for CS2030 (press enter without modificaiton): ')

        new_score1 = 0 if new_score1 == '' else int(new_score1)
        new_score2 = 0 if new_score2 == '' else int(new_score2)
        new_score3 = 0 if new_score3 == '' else int(new_score3)

        try:
            result = sc_session.execute(update(Score).where(Score.id == student_id).values(CS1030=new_score1, CS1100=new_score2, CS2030=new_score3))
            sc_session.commit()

            if result.rowcount > 0:
                print('\t \u2714 Record Updated Successfully')
            else:
                print('\t \u274C No record updated...')

        except Exception as e:
            sc_session.rollback()
            print("Error:", e)

        finally:
            sc_session.close()

    else:
        return

def registration():
    print ('=' * 24 + 'Registration' + '=' * 24)
    print('\t \u2666 1. Account Name is between 3 and 6 letters long ')
    print('\t \u2666 2. Account name\'s first letter must be capitalized')

    # Validate account name
    while True:
        account_name = input('Please Enter Account Name: ')
        result = c_session.execute(select(User).where(User.userid == account_name)).scalars().all()
        if not (username_check(account_name)):
            print('\t \u274c Account Name Not Valid!')
        elif len(result) > 0:
            print('\t \u274c Registration Failed! Account Already Exists')
        else:
            break

    print('\t \u2666 Password must starts with one of the following special characters !@#$%^&*')
    print('\t \u2666 Password must contain at least one digit, one lowercase letter and one uppercase letter')
    print('\t \u2666 Password is between 6 and 12 letters long')

    # Validate password
    while True:
        password = input('Please enter your Password: ')
        if not (check_password(password)):
            print('\t \u274c Password Not Valid!')
        else:
            hashed_pwd = hashlib.md5(password.encode())
            break

    # Create a record in the user table for the username and password
    u = User(userid=account_name, password=hashed_pwd.hexdigest())
    c_session.add(u)
    c_session.commit()
    print('\t \u2714 Registration Complete!')

def start():
    # read the file to display the menu
    content = read_file('welcome.txt')

    while True:
        code = input(content + '\nPlease select (1 - 3): ')
        if code == '1':
            login()
        elif code == '2':
            registration()
        elif code == '3':
            exit_system()
        else:
            print('\t \u274C Invalid Input')

if __name__ == '__main__':
    start()