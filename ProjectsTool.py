import random
import string
import re
import os
from datetime import date

SIZE_OF_PROJECT_ID=10
currentDate=date.today().strftime("%d/%m/%Y")

def create_new_project():
    global currentDate
    print_project_instructions()
    flags=[0,0,0]
    projectName=project_name_validation()
    projectDueDate=project_date_validation()
    while project_date_too_close(projectDueDate):
        print("Due date too close, please make sue date is at least 7 days after: "+currentDate)
        projectDueDate=project_date_validation()
    print("Due Date is valid!: "+projectDueDate)
    projectID="".join(random.choices(string.ascii_uppercase + string.digits, k=SIZE_OF_PROJECT_ID))
    print("ID generated for this project is: "+str(projectID))
    file = open('Projects.txt', 'a')
    data_dict = {'Project ID:':projectID,"Project name:":projectName,'Project due date:':projectDueDate}
    for key,value in data_dict.items():
        file.write(str(key) + " " + str(value)+'\n')
    file.close()
    print('Project name: ' + projectName + '\nProject due date: ' + projectDueDate, '\nProject ID: ' + projectID + "\nwere succesfully written to file!")

def print_project_instructions():
    global currentDate
    print("Instructions for new project:")
    print("1) Project name must only contain letters(both lower and upper case)")
    print("2) Projects are identified by a "+str(SIZE_OF_PROJECT_ID)+" digit random generated serial number containing uppercase letters and numbers")
    print("3) Project due date must be entered as followed: DD/MM/YYYY")
    print("4) Project due date must be at least 7 days from: "+currentDate+" (current date)")
    print("5) Projects with identical names are possible\n")
    
def project_name_validation():
    projectName=input("Enter project name\n")
    allowedCharachters=re.compile(r'[a-zA-Z\s]*$')
    while (not allowedCharachters.match(projectName)):
        projectName=input("Project name is not valid, please select a project name according to instructions\n")
    print("Project name is valid!")
    return projectName
    
def project_date_validation():
    dateFormat=re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
    projectDueDate=input("Enter project due date\n")
    while (not dateFormat.match(projectDueDate)):
        projectDueDate=input("Project Due date does not match format, please use DD/MM/YYYY \n")
    days=projectDueDate.split("/")[0]
    months=projectDueDate.split("/")[1]
    years=projectDueDate.split("/")[2]
    flags=[0,0]
    while (flags[0] == 0) or (flags[1] == 0):
        if (int(days) in range(1,31)):
            flags[0]=1
        else:
            days=input("days not in range, please enter a vlaue between 1 to 31\n")
        if (int(months) in range(1,13)):
            flags[1]=1
        else:
            months=input("months not in range, please enter a vlaue between 1 to 12\n")
    dateList=[days,months,years]
    projectDueDate="/".join(dateList)
    return projectDueDate
    
def project_date_too_close(projectDueDate):
    global currentDate
    currDay=int(currentDate.split("/")[0])
    currMonth=int(currentDate.split("/")[1])
    currYear=int(currentDate.split("/")[2])
    days=int(projectDueDate.split("/")[0])
    months=int(projectDueDate.split("/")[1])
    years=int(projectDueDate.split("/")[2])
    if years>currYear:
        return False
    elif years==currYear:
        if (months-currMonth)>1:
            return False
        elif (months-currMonth)==1:
            if (30+(currDay-days))>=7:
                return False
        elif months==currMonth:
            if days>=(currDay+7):
                return False              
    return True
    
def get_details_by_ID():
    search = 'Project ID: ' + (input("Enter Project ID to extract details:"))
    list = create_list_from_file('Projects.txt','t')
    try:
        idIndex = int(list.index(search))
    except ValueError:
        print('Project Id not found!')
    print(list[idIndex + 1])
    print(list[idIndex + 2])


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
    
def remove_duplicate_projects():
    print("This action will look for projects with the same Name and Due date and will remove them from file")
    print("Attention! removed projects cannot be restored")
    choice=input("Press Y or YES to delete, any other key to go back to menu\n")
    choice_list = ['y', 'yes', 'Y', 'YES']
    if choice in choice_list:
        projectDictList = []
        with open("Projects.txt", "r") as f:
            lines=f.readlines()
            intern_dict = {}
            for line in lines:
                (key, val) = line.split(": ")
                if key!="Project due date":
                    intern_dict[key]=val
                if key=="Project due date":
                    intern_dict[key]=val
                    projectDictList.append(intern_dict)
                    intern_dict = {}
            # print("Type of global_list: {0}\n".format(type(projectDictList)))
            # print(projectDictList)
            # print("\nType of elements inside global_list\n")
            # for i in projectDictList:
                # print("{0}\tType: {1}".format(i, type(i)))
                # print(projectDictList.index(i))
            projectDictList=[dict(t) for t in {tuple(d.items()) for d in projectDictList}]
            # print("Type of global_list: {0}\n".format(type(projectDictList)))
            # print(projectDictList)
            # print("\nType of elements inside global_list\n")
            # for i in projectDictList:
                # print("{0}\tType: {1}".format(i, type(i)))
                # print(projectDictList.index(i))  
            linesToRemove=[]
            for d in projectDictList:
                currDate=d['Project due date']
                currName=d['Project name']
                dictIndex=projectDictList.index(d)
                # print("d is: "+str(dictIndex))
                i=dictIndex+1
                for i in range(dictIndex+1,len(projectDictList)):
                    # print("i is: "+str(i))
                    if (currDate==projectDictList[i]['Project due date']) and (currName==projectDictList[i]['Project name']):
                        linesToRemove.append(i)
            # print("lines to remove: ")
            linesToRemove = list(dict.fromkeys(linesToRemove))
            # print(linesToRemove)
            for i in linesToRemove:
                # print("i is: "+str(i))
                if i>=len(projectDictList):
                    projectDictList.pop()
                else:
                    del projectDictList[i]
            # print("Type of global_list: {0}\n".format(type(projectDictList)))
            # print(projectDictList)
            # print("\nType of elements inside global_list\n")
            # for i in projectDictList:
                # print("{0}\tType: {1}".format(i, type(i)))
                # print(projectDictList.index(i))
        with open("Projects.txt", "w") as f:
            for line in projectDictList:
                for key,value in line.items():
                    f.write(str(key) + ": " + str(value))
        print("Duplicate Projects removed from file Projects.txt!")
                
            
            
       
def print_project_menu():
    print("Welcome to project management tool! please select an action")
    print("1.Create new project")
    print("2.Get project details by ID")
    print("3.Remove duplicate projects")
    
def project_tool_main():

    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:

        print_project_menu()
        choice = input("Enter 1-8 from the menu:\n")
        if choice == '1':
            create_new_project()
        elif choice == '2':
            get_details_by_ID()
        elif choice == '3':
            remove_duplicate_projects()
        else:
            print("Invalid input!")
        again = input("Would you like to preform another action?(Y/N)\n")

    print("Goodbye!")
    
     
    
project_tool_main()
