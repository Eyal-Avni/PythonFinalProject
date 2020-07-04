def set_employee_password(emploID, name):
    password=input("Enter "+name+" password:")
    file=open("passwords.bin",'ab')
    file.write(emploID.encode()+":".encode()+password.encode()+"\n".encode())
    file.close()

def get_employee_info():
    first=input("Enter employee's name: ")
    last = input("Enter " +first+ "'s last name: ")
    full_name=first+" "+last
    ID = input("Enter " + full_name + "'s ID number: ")
    department = input("Enter "+full_name+" depatment: ")
    dob = input("Enter "+full_name+"'s date of birth: ")
    email= input("Enter "+full_name+"'s email adress: ")
    set_employee_password(ID,full_name)

    data_list=[]
    data_list.append(ID)
    data_list.append(full_name)
    data_list.append(department)
    data_list.append(dob)
    data_list.append(email)

    return data_list
def update_file_from_list(list, filename_to_update):
    file = open('temp.txt', 'w')
    for item in list:
        file.write(str(item) + '\n')

    file.close()
    os.remove(filename_to_update)
    os.rename('temp.txt', filename_to_update)
def create_new_file_from_list(list,filename):

    file = open(filename+'.txt',"a")
    for item in list:
        file.write(str(item) + '\n')

    file.close()

def read_bin_to_list(filename):
    file=open(filename+'.bin','rb')
    flist=[]
    for bin_line in file:
        line=bin_line.decode('ascii')
        flist.append(line.rstrip('\n'))

    file.close()

    return flist
def create_list_from_file(filename,mode):
    try:
        if mode=='t':
            file = open(str(filename), 'r')
        else:
            file= open(filename+'.bin','rb')
    except IOError:
        print('Error! Check file ' + str(filename))

    list = file.readlines()

    index = 0
    file.close()

    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1

    return list

def create_passw_dici(filename):
    i=0
    passlist=read_bin_to_list(filename)
    dici = {}
    while i<len(passlist):
        splited=passlist[i].split(':')
        dici[splited[0]]=splited[1]
        i+=1

    return dici
    input()




##create_new_file_from_list(get_employee_info(),'Employees')
create_passw_dici('passwords')
input()