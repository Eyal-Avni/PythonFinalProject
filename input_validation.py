import string
def check_email_val(string):
    length = False
    at_sign = False
    dot = False

    if len(string) >=5:
        length = True

    for ch in string:
        if ch=='@':
            at_sign = True

        if ch=='.':
            dot = True

    if length and at_sign and dot:
        return True
    else:
        return False

def check_gender_input(string):
    choice_list=['Male','Female']
    if string not in choice_list:
        return False
    return True

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

def check_ID(string):
    if len(str(string))<9 or not string.isdigit():
        return 0
    else:
        return 1

def check_name(string):
    if string.isalpha():
        return 1
    else:
        return 0


