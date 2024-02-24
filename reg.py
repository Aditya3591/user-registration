import re

def validate_name(name):

    pattern=r'[A-Z][a-z]{2,}'

    if re.match(pattern,name):
        return True
    else:
        return False
    

first_name=input("enter the first name :")
last_name=input("enter the last name :")


if validate_name(first_name) and validate_name(last_name):

    print("the name is valid")

else:
    print("the name is not valid")

