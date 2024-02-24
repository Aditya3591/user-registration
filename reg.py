import re

def validate_name(name):

    pattern=r'[A-Z][a-z]{2,}'

    if re.match(pattern,name):
        return True
    else:
        return False
    
def validate_email(email):


    email_pattern=re.compile("[^0-9][a-z0-9\-\+]+[.a-z0-9]@[a-z0-9]+.[a-z]+[.in]")
    email_valid=email_pattern.match(email)

    if email_valid:
        print("the email is valid")
    else:
        print("the email is not valid")


first_name=input("enter the first name :")
last_name=input("enter the last name :")


if validate_name(first_name) and validate_name(last_name):

    print("the name is valid")

else:
    print("the name is not valid")

email=input("enter the email :")
validate_email(email)