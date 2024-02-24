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

def validate_ph_number(phn_num):

    phn_num_pattern=re.compile('^91 \d{10}$')
    phn_num_valid=phn_num_pattern.match(phn_num)

    if phn_num_valid:
        print("the number is valid")

    else:

        print("the number is not valid")

def validate_password(password):

    password_pattern = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#?$])[A-Za-z\d@#?$]{8,}$')
    paswordvalid=password_pattern.match(password)
    if paswordvalid:
        print("passowrd id valid")
    else:
        print("password is invalid")

    

first_name=input("enter the first name :")
last_name=input("enter the last name :")


if validate_name(first_name) and validate_name(last_name):

    print("the name is valid")

else:
    print("the name is not valid")

email=input("enter the email :")
validate_email(email)

phn_num=(input("enter the phone number"))
validate_ph_number(phn_num)

password=(input("enter the password"))
validate_password(password)