import os
import json

def update_bin_file_from_list(list,filename_to_update):
    file = open('temp.txt', 'wb')
    for item in list:
        file.write(str(item).encode() + '\n'.encode())

    file.close()
    os.remove(filename_to_update)
    os.rename('temp.txt', filename_to_update)
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
    os.remove(filename_to_update)
    os.rename('temp', filename_to_update)
def add_to_file_from_list(list,filename):

    file = open(filename,"a")
    for item in list:
        file.write(str(item) + '\n')

    file.close()
def binfile_to_list(filename):
    file=open(filename,'rb')
    flist=[]
    for bin_line in file:
        line=bin_line.decode('ascii')
        flist.append(line.rstrip('\n'))

    file.close()

    return flist
def binfile_to_dici(filename):#check
    i=0
    passlist=binfile_to_list(filename)
    dici = {}
    while i<len(passlist):
        splited=passlist[i].split(':')
        dici[splited[0]]=splited[1]
        i+=1

    return dici#
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
    
    
def update_file_from_list(list, filename_to_update):
    with open("temp.txt", "w") as f:
        for line in list:
            if type(line) is not dict:
                splitString=line.split(": ")
                tempString=str('{"'+splitString[0]+'" : "'+splitString[1]+'"}')
                tempDict = json.loads(tempString)
                line=tempDict
            for key,value in line.items():
                f.write(str(key) + ": " + str(value)+"\n")
    try:
        os.remove(filename_to_update)
    except(FileNotFoundError):
        print("file not found!")
    os.rename('temp.txt', filename_to_update)
