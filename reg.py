import re

def validate_name(frist_name):

    pattern=r'[A-Z][a-z]{2,}'

    if re.match(pattern,first_name):
        return True
    else:
        return False
    

first_name=input("enter the first name :")
if validate_name(first_name):

    print("valid frist name")

else:
    print("the name is not valid")

