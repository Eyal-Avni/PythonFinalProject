import string
import re
#even though regular expression are not taught in this course we have used them in certain functions ONLY for the purpose of formating strings
#for example to make sure a date is of the DD/MM/YYYY format. this could have been done by creating many string variables and appending them, but this way is shorter and more elegant


#This function validates employee Email structure (XXX@XXX.XXX)
def check_email_val(string):
    length = False
    at_sign = False
    dot = False

    if len(string) >= 5:
        length = True

    for ch in string:
        if ch == '@':
            at_sign = True

        if ch == '.':
            dot = True

    if length and at_sign and dot:
        return True
    else:
        return False
        
#This function validates gender option choices
def check_gender_input(string):
    choice_list = ['Male', 'Female']
    if string not in choice_list:
        return False
    return True

#This function validates employee password according to insturctions
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

#This function validates employee ID structure
def check_ID(string):
    if len(str(string)) < 9:
        return 0
    else:
        return 1


#This function validates employee name is alphabetical only
def check_name(string):
    if string.isalpha():
        return 1
    else:
        return 0

#This function validates project name is according to insturctions
def project_name_validation():
    projectName = input("Enter project name\n")
    allowedCharachters = re.compile(r'[a-zA-Z\s]*$')
    while (not allowedCharachters.match(projectName)):
        projectName = input("Project name is not valid, please select a project name according to instructions\n")
    print("Project name is valid!")
    return projectName

#This function validates project Due date is according to insturctions
def project_date_validation():
    dateFormat = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
    projectDueDate = input("Enter project due date\n")
    while (not dateFormat.match(projectDueDate)):
        projectDueDate = input("Project Due date does not match format, please use DD/MM/YYYY\n")
    days = projectDueDate.split("/")[0]
    months = projectDueDate.split("/")[1]
    years = projectDueDate.split("/")[2]
    flags = [0, 0]
    while (flags[0] == 0) or (flags[1] == 0):
        if (int(days) in range(1, 31)):
            flags[0] = 1
        else:
            days = input("days not in range, please enter a vlaue between 1 to 30\n")
        if (int(months) in range(1, 13)):
            flags[1] = 1
        else:
            months = input("months not in range, please enter a vlaue between 1 to 12\n")
    dateList = [days, months, years]
    projectDueDate = "/".join(dateList)
    return projectDueDate


