ROWS_OF_INFO_PER_PERSON=6
import os



def set_employee_password(emploID, name):
    password=input("Enter "+name+" password:")
    file=open("passwords.bin",'ab')
    file.write(emploID.encode()+":".encode()+password.encode()+"\n".encode())
    file.close()

def update_bin_file_from_list(list):
    file = open('temp.txt', 'wb')
    for item in list:
        file.write(str(item) + '\n')

    file.close()
    os.remove(filename_to_update)
    os.rename('temp.txt', filename_to_update)

def print_password_instructions():
    print('Attention!')
    print('Your password must be at least 7 characters long')
    print('Your password must contain at least one uppercase letter')
    print('Your password must contain at least one number digit ')

def get_employee_info():
    first=input("Enter employee's first name: ")
    last = input("Enter " +first+ "'s last name: ")
    full_name=first+" "+last
    full_name_2='Full name:'+full_name
    ID = 'ID number:'+input("Enter " + full_name + "'s ID number: ")
    phone = 'Phone number:' + input("Enter " + full_name + "'s phone number: ")
    department ='Department:'+input("Enter "+full_name+" depatment: ")
    dob = 'Date of birth:'+input("Enter "+full_name+"'s date of birth: ")
    email= 'Email adress:'+input("Enter "+full_name+"'s email adress: ")
    inedx=ID.find(':')+1
    ID_2=ID[inedx: ]
    set_employee_password(ID_2,full_name)

    data_list=[]
    data_list.append(ID)
    data_list.append(full_name_2)
    data_list.append(department)
    data_list.append(dob)
    data_list.append(email)
    data_list.append(phone)

    return data_list

def update_file_from_list(list, filename_to_update,mode):
    if mode=='b':
        file = open('temp', 'wb')
    else:
        file = open('temp', 'w')

    if mode=='b':
        for item in list:
            file.write(str(item).encode() + '\n'.encode())
    else:
         for item in list:
            file.write(str(item) + '\n')

    file.close()
    if mode=='b':
        os.remove(filename_to_update+'.bin')
        os.rename('temp', filename_to_update+'.bin')
    else:
        os.remove(filename_to_update)
        os.rename('temp', filename_to_update)

def check_password(string):
    length = False
    upper = False
    digit = False

    if len(string) >= 7:
        length = True

    for ch in string:
        if ch.isupper():
            upper = True

        if ch.isdigit():
            digit = True

    if length and upper and digit:
        return True
    else:
        print('Invalid password strength!')
        return False

def check_email_val(string):
    length = False
    at_sign = False
    dot = False

    if len(string) >=5:
        length = True

    for ch in string:
        if ch=='@'():
            at_sign = True

        if ch=='.'():
            dot = True

    if length and at_sign and dot:
        return True
    else:
        print('Invalid email adress!')
        return False

def check_dob(string):



def dici_to_list(dici):

    res=[]
    keys = list(dici.keys())
    value = list(dici.values())
    i=0
    lennn=len(dici)

    while i<len(dici):
        res.append(keys[i]+':'+value[i])
        i+=1

    return res

def change_password(pass_filename):
    search=input("Enter the employee's ID")
    pass_dici = binfile_to_dici(pass_filename)


    if search in pass_dici:
        flag = 1
        while (flag == 1):
            print_password_instructions()
            new_password = (input("Enter the new password:"))
            if check_password(new_password):
                flag = 0

        pass_dici[search] = new_password
        pass_list=dici_to_list(pass_dici)
        update_file_from_list(pass_list,'passwords','b')

        print('Password has been changed successfully!')


    else:
        print('ID was not found!')

def add_to_file_from_list(list,filename):

    file = open(filename+'.txt',"a")
    for item in list:
        file.write(str(item) + '\n')

    file.close()

def binfile_to_list(filename):
    file=open(filename+'.bin','rb')
    flist=[]
    for bin_line in file:
        line=bin_line.decode('ascii')
        flist.append(line.rstrip('\n'))

    file.close()

    return flist

def txt_file_to_list(filename):

    try:
        file = open(filename,'r')
    except IOError:
         print('Error! Check file '+ filename)

    list = file.readlines()
    index = 0

    file.close()

    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1

    return list

def binfile_to_dici(filename):
    i=0
    passlist=binfile_to_list(filename)
    dici = {}
    while i<len(passlist):
        splited=passlist[i].split(':')
        dici[splited[0]]=splited[1]
        i+=1

    return dici

def delete_employee(filename):
    list = txt_file_to_list(filename)
    search ='ID number:'+(input("Enter ID number to delete:"))
    try:
        index = int(list.index(search))
    except ValueError:
        print("Id wasn't found!")

    i = 0

    while i < ROWS_OF_INFO_PER_PERSON:  # כמספר השורות מידע על כל בן אדם
        list.remove(list[index])  # לא מעדכנים את האינדקס למחיקה כי לאחר כל מחיקה הרשימה מצטמצמת ומעדכנת אינדקסים
        i += 1

    update_file_from_list(list,'Employees','t')

def change_depart(filename):
    list = txt_file_to_list(filename)
    search = 'ID number:'+(input("Enter ID number to update:"))
    try:
        idIndex = int(list.index(search))
    except ValueError:
        print("Id wasn't found!")
    new_dept= (input("Enter the new department:"))
    dept_index = int(idIndex + 2)
    list[dept_index] = 'Department:' + str(new_dept)
    update_file_from_list(list,'Employees.txt','t')



def print_menu():
    print("Hello ! what would you like to do?  ")
    print("1.Open new employee card")
    print("2.Change employee's password")
    print("3.Delete employee")
    print("4.Chnage employee's department ")





def main():



    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:

        print_menu()
        choice = input("Enter 1-8 from the menu:")
        if choice == '1':
            info=get_employee_info()
            add_to_file_from_list(info, 'Employees')

        elif choice == '2':
            change_password('passwords')

        elif choice == '3':
            delete_employee('Employees.txt')
        elif choice == '4':
            change_depart('Employees.txt')
        elif choice == '5':
            print("There are currently " + str(get_num_of_guests()) + " guests!\n")
        elif choice == '6':
            show_availability_pie()
        elif choice == '7':
            set_password()
        elif choice == '8':
            change_password()
        else:
            print("Invalid input!")
        again = input("Would you like to preform another action?(Y/N) ")

    print("Goodbye!")



main()
