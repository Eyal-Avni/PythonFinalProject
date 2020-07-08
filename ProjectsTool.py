import random
import string
import re
import os
from datetime import date
import datetime
import file_manipuli
import input_validation
import matplotlib.pyplot as plt

SIZE_OF_PROJECT_ID=10
SIZE_OF_ENTRY_IN_PROJECT_LIST=4
currentDate=date.today().strftime("%d/%m/%Y")

def create_new_project():
    global currentDate
    print_project_instructions()
    projectName=input_validation.project_name_validation()
    projectDueDate=input_validation.project_date_validation()
    while project_date_too_close(projectDueDate):
        print("Due date too close, please make sure date is at least 7 days after: "+currentDate+" (current date)")
        projectDueDate=input_validation.project_date_validation()
    print("Due Date is valid!: "+projectDueDate)
    projectID="".join(random.choices(string.ascii_uppercase + string.digits, k=SIZE_OF_PROJECT_ID))
    print("ID generated for this project is: "+str(projectID))  
    file = open('Projects.txt', 'a')
    data_dict = {'Project ID:':projectID,"Project name:":projectName,"Project acceptance date:":currentDate,'Project due date:':projectDueDate}
    for key,value in data_dict.items():
        file.write(str(key) + " " + str(value)+'\n')
    file.close()
    print('Project name: ' + projectName+ '\nProject acceptance date: '+currentDate + '\nProject due date: ' + projectDueDate, '\nProject ID: ' + projectID + "\nwere succesfully written to file!")

def print_project_instructions():
    global currentDate
    print("----------------------\nInstructions for new project:")
    print("1) Project name must only contain letters(both lower and upper case are acceptable)")
    print("2) Projects are identified by a "+str(SIZE_OF_PROJECT_ID)+" digit random generated serial number containing uppercase letters and numbers")
    print("3) Project due date must be entered as follows: DD/MM/YYYY, assuming all months have 30 days")
    print("4) Project due date must be at least 7 days from: "+currentDate+" (current date)")
    print("5) Projects with identical names are possible\n")
    
    
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
            if (30-currDay+days)>=7:
                return False
        elif months==currMonth:
            if days>=(currDay+7):
                return False              
    return True
    
def get_details_by_ID():
    search = 'Project ID: ' + (input("Enter Project ID to extract details:"))
    list = file_manipuli.txt_file_to_list('Projects.txt')
    try:
        idIndex = int(list.index(search))
    except (ValueError):
        print('Project Id not found!')
        return()
    print(list[idIndex + 1])
    print(list[idIndex + 2])
    print(list[idIndex + 3])

    
def remove_duplicate_projects():
    print("This action will look for projects with the same Name and Due date and will remove them from file")
    print("Attention! removed projects cannot be restored and will not move to terminated file!")
    choice=input("Press Y or YES to delete, any other key to go back to menu\n")
    choice_list = ['y', 'yes', 'Y', 'YES']
    if choice in choice_list:
        projectDictList = []
        with open("Projects.txt", "r") as f:
            lines=f.readlines()
            intern_dict = {}
            for line in lines:
                line=line.strip()
                (key, val) = line.split(": ")
                if key!="Project due date":
                    intern_dict[key]=val
                if key=="Project due date":
                    intern_dict[key]=val
                    projectDictList.append(intern_dict)
                    intern_dict = {}
            projectDictList=[dict(t) for t in {tuple(d.items()) for d in projectDictList}] 
            linesToRemove=[]
            for d in projectDictList:
                currDate=d['Project due date']
                currName=d['Project name']
                dictIndex=projectDictList.index(d)
                i=dictIndex+1
                for i in range(dictIndex+1,len(projectDictList)):
                    if (currDate==projectDictList[i]['Project due date']) and (currName==projectDictList[i]['Project name']):
                        linesToRemove.append(i)
            linesToRemove = list(dict.fromkeys(linesToRemove))
            for i in linesToRemove:
                if i>=len(projectDictList):
                    projectDictList.pop()
                else:
                    del projectDictList[i]
        file_manipuli.update_file_from_list(projectDictList,"Projects.txt")
        print("Duplicate Projects removed from file Projects.txt!")
        
def show_projects(file,headline):
    print("projects in "+headline+" Projects file :")
    list = file_manipuli.txt_file_to_list(file)
    for i in list:
        if ("Project ID") in i:
            print("----------------------")
        print(i)
    print("----------------------")
        
def terminate_project():
    print("Terminated projects will be removed from current project file and written to terminated projects file")
    choice=input("Press Y or YES to begin termination process, any other key to go back to menu\n")
    choice_list = ['y', 'yes', 'Y', 'YES']
    if choice in choice_list:
        search = 'Project ID: ' + (input("Enter Project ID you wish to terminate:"))
        search=search.rstrip('\n')
        list = file_manipuli.txt_file_to_list('Projects.txt')
        termiList=file_manipuli.txt_file_to_list('TermiProjects.txt')
        try:
            idIndex = int(list.index(search))
        except ValueError:
            print('Project Id not found!')
            return()
        for i in range(SIZE_OF_ENTRY_IN_PROJECT_LIST):
            termiList.append(list[idIndex])
            list.remove(list[idIndex])
        global currentDate
        termiList.append("Project termination date: "+currentDate)
        file_manipuli.update_file_from_list(list,'Projects.txt')
        file_manipuli.update_file_from_list(termiList,'TermiProjects.txt')
        print(search+" has been terminated!")
    
def edit_project_details():
    search = 'Project ID: ' + (input("Enter Project ID you wish to edit:\n"))
    search=search.rstrip('\n')
    list = file_manipuli.txt_file_to_list('Projects.txt')
    try:
        idIndex = int(list.index(search))
    except ValueError:
        print('Project Id not found!')
        return()
    repeatChoices=['y', 'yes', 'Y', 'YES']
    repeat='y'
    while repeat in repeatChoices:
        choice=input("choose action: \nPress D to edit due date\nPress N to edit name\n")
        choice_list = ['d','D','date','Date','n','N','name','Name']
        if choice in ['d','D','date','Date']:
            print("Current "+ list[idIndex+3])
            date=input_validation.project_date_validation()
            list[idIndex+3]="Project due date: "+date
            print("Updated "+list[idIndex+3])
                 
        elif choice in ['n','N','name','Name']:
            print("Current "+ list[idIndex+1])
            name=input_validation.project_name_validation()
            list[idIndex+1]="Project name: "+name
            print("Updated "+list[idIndex+1])
        else:
            print("Invalid input! please follow instructions")   
        repeat=input("Would you like to preform another action?\n(press Yes or Y to edit more details, anything else to save edited information and return to menu)\n")
    file_manipuli.update_file_from_list(list,'Projects.txt')
    print("All updates in: "+search+" has been succesfully made and written to Projects.txt!\n")
    

def get_time_list(lookFor):
    list = file_manipuli.txt_file_to_list('TermiProjects.txt')
    handleList=[]
    flag=[0,0]
    for i in list:
        if (lookFor) in i:
            accDate=i.split(": ")
            accDay=int(accDate[1].split("/")[0])
            accMonth=int(accDate[1].split("/")[1])
            accYear=int(accDate[1].split("/")[2])
            accDateObj=datetime.date(accYear, accMonth, accDay)
            flag[0]=1
            # print("due date: "+str(dueDate))
        if ("Project termination date") in i:
            termiDate=i.split(": ")
            termiDay=int(termiDate[1].split("/")[0])
            termiMonth=int(termiDate[1].split("/")[1])
            termiYear=int(termiDate[1].split("/")[2])
            termDateObj=datetime.date(termiYear, termiMonth, termiDay)
            flag[1]=1
            # print("termi date: "+str(termiDate))
        if flag==[1,1]:
            handleTimeObj=termDateObj-accDateObj
            handleList.append(int(handleTimeObj.total_seconds()/24/60/60))
            flag=[0,0]           
    return handleList
    
def get_late_graph_list():
    handleList=get_time_list("Project due date:")
    graphList=[0,0]
    for i in handleList:
        if i<0:
            graphList[0]=graphList[0]+1
        else:
            graphList[1]=graphList[1]+1
    return graphList
    
    
def get_handle_graph_list():
    handleList=get_time_list("Project acceptance date")
    graphList=[0,0,0,0]
    for i in handleList:
        if i<=14:
            graphList[0]=graphList[0]+1
        elif i<=30:
            graphList[1]=graphList[1]+1
        elif i<=120:
            graphList[2]=graphList[2]+1
        elif i>120:
            graphList[3]=graphList[3]+1
    return graphList
        

def show_handle_time_chart():
    fig,ax = plt.subplots()
    plt.title('Project Handle Time Chart')
    timeLabels = ['two weeks\n or less', 'two weeks\n to \none month','one month\n to \nsix months','six months\n or more']
    data=get_handle_graph_list()
    timeBar=ax.bar(timeLabels,data,color=['green', 'yellow', 'orange', 'red'],edgecolor='black')
    ax.set_ylabel('Number of projects') 
    ax.set_xlabel('Time took to complete ') 
    plt.show()
    
def show_on_time_completion_percentage():
    plt.title('On-Time Completion Chart')
    data = get_late_graph_list()
    Labels = ['Completed on time','Completed late',]
    explode = (0, 0.4)
    plt.pie(data, labels=Labels, explode=explode, startangle=90, autopct='%d%%',colors=["Green","red"])
    plt.show()
    

def print_project_menu():
    print("Welcome to project management tool! please select an action")
    print("1.Create new project")
    print("2.Get project details by ID")
    print("3.Terminate project")
    print("4.Edit project details")
    print("5.Check for projects that are due this week")
    print("6.Show current projects")
    print("7.Show terminated projects")
    print("8.Remove duplicate projects")
    print("9.Show Handle Time chart")
    print("10.Show On-Time Completion Chart")
    
    
    
def check_expiring_projects():
    global currentDate
    list = file_manipuli.txt_file_to_list('Projects.txt')
    noExpiring=True
    for i in list:
        if ("Project ID") in i:
            ID=i.split(": ")
        if ("Project name") in i:
            name=i.split(": ")
        if ("Project due date") in i:
            date=i.split(": ")
            if project_date_too_close(date[1]):
                noExpiring=False
                print("Warning! the following project is reaching it's due date (less than 7 days):")
                print(ID)
                print(name)
                print(date)
    if noExpiring:
        print("No projects are due to this week")
          
    
def project_tool_main():

    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:

        print_project_menu()
        choice = input("Enter your selection from the menu:\n")
        if choice == '1':
            create_new_project()
        elif choice == '2':
            get_details_by_ID()
        elif choice == '3':
            terminate_project()
        elif choice == '4':
            edit_project_details()
        elif choice == '5':
            check_expiring_projects()
        elif choice == '6':
            show_projects("Projects.txt","Current")
        elif choice == '7':
            show_projects("TermiProjects.txt","Terminated")
        elif choice == '8':
            remove_duplicate_projects()
        elif choice == '9':
            show_handle_time_chart()
        elif choice == '10':
            show_on_time_completion_percentage()
        else:
            print("Invalid input!")
        again = input("----------------------\nMain Project Tool Menu:\nWould you like to preform another action?(Y/N)\n")

    print("Goodbye!")
       
    
project_tool_main()
