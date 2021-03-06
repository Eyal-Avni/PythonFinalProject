ROWS_OF_INFO_PER_PERSON=6
EMPLOYEES_FILE_GIVEN_NAME='Employees.txt'
PASSWORD_FILE_GIVEN_NAME='Passwords.bin'
SIZE_OF_INITAIL_PASS=7
import random
import matplotlib.pyplot as plt
import input_validation
import file_manipuli
import re
import string

def set_employee_password(emploID):

    digits_from_id=emploID[:3]
    password ="".join(random.choices(string.ascii_uppercase + string.digits, k=SIZE_OF_INITAIL_PASS))

    file=open(PASSWORD_FILE_GIVEN_NAME,'ab')
    file.write(emploID.encode()+":".encode()+digits_from_id.encode()+password.encode()+"\n".encode())
    file.close()

def get_employee_info():

    flags=[0,0,0,0,0]

    while flags[4]==0:
        try:
            first=input("Enter employee's first name: ")
            temp=1/input_validation.check_name(first)
            last = input("Enter " +first+ "'s last name: ")
            flags[4]=1/input_validation.check_name(last)
        except ZeroDivisionError:
            print('Error! name must contain alphabet characters only!')

    full_name=first+" "+last

    while flags[0]==0:
        try:
            ID =int(input("Enter " + full_name + "'s ID number: "))
            flags[0]=int(1/input_validation.check_ID(ID))
        except ValueError:
            print('Error! invalid input, numbers only!')
        except ZeroDivisionError:
            print('Error! invalid ID length!')

    while flags[1]==0:
        gender = input('Enter gender(Male/Female):')
        if input_validation.check_gender_input(gender):
            flags[1]=1
        else:
            print("Invalid gender input!")

    while flags[2] == 0:
        try:
            phone = int(input("Enter " + full_name + "'s phone number: "))
            flags[2] = 1
        except ValueError:
            print('Error! invalid input, numbers only!')

    department =input("Enter "+full_name+" depatment: ")

    while flags[3]==0:
        email = input("Enter " + full_name + "'s email address: ")
        if input_validation.check_email_val(email):
            flags[3]=1
        else:
            print("Invalid email address!")

    set_employee_password(str(ID))

    data_list=[]
    data_list.append('ID number:'+str(ID))
    data_list.append('Full name:'+full_name)
    data_list.append('Gender:'+gender)
    data_list.append('Department:'+department)
    data_list.append('Email address:'+email)
    data_list.append('Phone number:'+str(phone))

    return data_list

def change_password(pass_filename):
    search=input("Enter the employee's ID:")
    pass_dici = file_manipuli.binfile_to_dici(pass_filename)


    if search in pass_dici:
        flag = 1
        while (flag == 1):
            print_password_instructions()
            new_password = (input("Enter the new password:"))
            if input_validation.check_password(new_password):
                flag = 0

        pass_dici[search] = new_password
        pass_list=file_manipuli.dici_to_list(pass_dici)
        file_manipuli.update_file_from_list(pass_list,PASSWORD_FILE_GIVEN_NAME,'t')

        print('Password has been changed successfully!')


    else:
        print('ID was not found!')

def delete_employee(empl_filename,pass_filename):
    list = file_manipuli.txt_file_to_list(empl_filename)
    flag=0
    while flag==0:
        search =(input("Enter ID number to delete:"))
        try:
            index = int(list.index('ID number:'+search))
            flag=1
        except ValueError:
            print("Id wasn't found!")

    i = 0

    while i < ROWS_OF_INFO_PER_PERSON:  # כמספר השורות מידע על כל בן אדם
        list.remove(list[index])  # לא מעדכנים את האינדקס למחיקה כי לאחר כל מחיקה הרשימה מצטמצמת ומעדכנת אינדקסים
        i += 1
    file_manipuli.update_file_from_list(list,empl_filename,'t')

    pass_list=file_manipuli.binfile_to_list(pass_filename)
    i=0
    while i<len(pass_list):
        if pass_list[i].startswith(search):
            pass_list.remove(pass_list[i])
        i+=1

    file_manipuli.update_bin_file_from_list(pass_list,PASSWORD_FILE_GIVEN_NAME)
    print('The file has been updated!')

def change_depart(empl_filename):
    list = file_manipuli.txt_file_to_list(empl_filename)
    search = 'ID number:'+(input("Enter ID number to update:"))
    try:
        idIndex = int(list.index(search))
    except ValueError:
        print("Id wasn't found!")
    new_dept= (input("Enter the new department:"))
    dept_index = int(idIndex + 3)
    list[dept_index] = 'Department:' + str(new_dept)
    file_manipuli.update_file_from_list(list,EMPLOYEES_FILE_GIVEN_NAME,'t')
    print("Department updated!\n")

def get_phone_by_ID(empl_filename):
    search = 'ID number:' + (input("Enter ID number to extract phone number:"))
    list = file_manipuli.txt_file_to_list(empl_filename)

    try:
        idIndex = int(list.index(search))

    except ValueError:
        print('Id not found!')

    print(list[idIndex + 5])

def get_email_by_name(empl_filename):
    search = 'Full name:'+ (input("Enter full name to extract email address:"))
    list = file_manipuli.txt_file_to_list(empl_filename)

    try:
        idIndex = int(list.index(search))

    except ValueError:
        print('Id not found!')

    print(list[idIndex + 3])

def get_mf_ratio():
    data_list=file_manipuli.txt_file_to_list('Employees.txt')
    length=len(data_list)
    i=0
    male_count=0
    female_count=0
    while i<length:
        if data_list[i].find('Male')!=-1:
            male_count+=1
        elif data_list[i].find('Female')!=-1:
            female_count+=1

        i+=1
    values = [male_count, female_count]
    Labels = ['male count', 'female count']
    explode = (0, 0.1)
    colors=['orange','pink']
    plt.pie(values, labels=Labels, explode=explode, startangle=120, autopct='%.1f%%',colors=colors)
    try:
        ratio=float(male_count/female_count)
    except ZeroDivisionError:
        print('No females were found in the company!')
        return

    plt.title('Male/Female ratio:\n'+str(ratio))

    plt.show()

def show_emp_name_list(empl_filename):
    list=file_manipuli.txt_file_to_list(empl_filename)
    emp_index=1
    i=1
    j=0
    print('Employees list:')
    while j<len(list):

        print(str(emp_index)+'.'+list[i+j].strip('Full name'))
        emp_index+=1
        j+=6

def print_menu():
    print("Welcome to Employees Management Tool! please select an action")
    print("1.Open new employee card")
    print("2.Change employee's password")
    print("3.Chnage employee's department ")
    print("4.Show employee's phone number by ID ")
    print("5.Show employee's email by full name")
    print("6.Delete employee")
    print("7.Show Male/Female ratio")
    print("8.Show Employee's name list\n")
    print("0.Return to Sapiens Information System menu")
    print("-------------------------------------------")

def print_password_instructions():
    print('Attention!')
    print('Your password must be at least 7 characters long')
    print('Your password must contain at least one uppercase letter')
    print('Your password must contain at least one number digit ')

def employee_main():



    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:

        print_menu()
        choice = input("Enter your selection from the menu:")
        if choice == '1':
            info=get_employee_info()
            file_manipuli.add_to_file_from_list(info,EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '2':
            change_password(PASSWORD_FILE_GIVEN_NAME)
        elif choice == '3':
            change_depart(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '4':
            get_phone_by_ID(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '5':
            get_email_by_name(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '6':
            delete_employee(EMPLOYEES_FILE_GIVEN_NAME, PASSWORD_FILE_GIVEN_NAME)
        elif choice == '7':
            get_mf_ratio()
        elif choice=='8':
            show_emp_name_list(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice=='0':
            return
        else:
            print("Invalid input!")
        again = input("----------------------\nEmployee Tool Menu:\nWould you like to preform another action?(Y/N)\n")
