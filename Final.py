ROWS_OF_INFO_PER_PERSON=6
EMPLOYEES_FILE_GIVEN_NAME='Employees.txt'
PASSWORD_FILE_GIVEN_NAME='Passwords.bin'
import os
import matplotlib.pyplot as plt
import input_validation
import file_manipuli


def set_employee_password(emploID, name):
    flag=0
    while flag==0:
        password=input("Enter "+name+" password:")
        if input_validation.check_password(password):
            flag=1
    file=open(PASSWORD_FILE_GIVEN_NAME,'ab')
    file.write(emploID.encode()+":".encode()+password.encode()+"\n".encode())
    file.close()

def get_employee_info():
    first=input("Enter employee's first name: ")
    last = input("Enter " +first+ "'s last name: ")
    full_name=first+" "+last

    flags=[0,0,0,0]
    while flags[0]==0:
        try:
            ID =int(input("Enter " + full_name + "'s ID number: "))
            flags[0]=1
        except ValueError:
            print('Error! invalid input, numbers only!')


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
        email = input("Enter " + full_name + "'s email adress: ")
        if input_validation.check_email_val(email):
            flags[3]=1
        else:
            print("Invalid email adress!")

    set_employee_password(str(ID),full_name)

    data_list=[]
    data_list.append('ID number:'+str(ID))
    data_list.append('Full name:'+full_name)
    data_list.append('Gender:'+gender)
    data_list.append('Department:'+department)
    data_list.append('Email adress:'+email)
    data_list.append('Phone number:'+str(phone))

    return data_list

def change_password(pass_filename):
    search=input("Enter the employee's ID")
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
        file_manipuli.update_file_from_list(pass_list,PASSWORD_FILE_GIVEN_NAME,'b')

        print('Password has been changed successfully!')


    else:
        print('ID was not found!')

def delete_employee(filename):
    list = file_manipuli.txt_file_to_list(filename)
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
    file_manipuli.update_file_from_list(list,EMPLOYEES_FILE_GIVEN_NAME,'t')

    pass_list=file_manipuli.binfile_to_list(PASSWORD_FILE_GIVEN_NAME)
    i=0
    while i<len(pass_list):
        if pass_list[i].startswith(search):
            pass_list.remove(pass_list[i])
        i+=1

    file_manipuli.update_bin_file_from_list(pass_list,PASSWORD_FILE_GIVEN_NAME)

def change_depart(filename):
    list = file_manipuli.txt_file_to_list(filename)
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
    ratio=float(male_count/female_count)
    plt.title('Male/Female ratio:\n'+str(ratio))

    plt.show()

def print_menu():
    print("Hello ! what would you like to do?  ")
    print("1.Open new employee card")
    print("2.Change employee's password")
    print("3.Chnage employee's department ")
    print("4.Delete employee")
    print("5.Show Male/Female ratio")

def print_password_instructions():
    print('Attention!')
    print('Your password must be at least 7 characters long')
    print('Your password must contain at least one uppercase letter')
    print('Your password must contain at least one number digit ')

def main():



    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:

        print_menu()
        choice = input("Enter 1-5 from the menu:")
        if choice == '1':
            info=get_employee_info()
            file_manipuli.add_to_file_from_list(info,EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '2':
            change_password(PASSWORD_FILE_GIVEN_NAME)
        elif choice == '3':
            change_depart(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '4':
            delete_employee(EMPLOYEES_FILE_GIVEN_NAME)
        elif choice == '5':
            get_mf_ratio()

        else:
            print("Invalid input!")
        again = input("Would you like to preform another action?(Y/N) ")

    print("Goodbye!")



main()
