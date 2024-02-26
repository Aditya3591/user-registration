import re
import logging

def set_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(lineno)s:%(message)s")
    file_logger = logging.FileHandler(filename='app.log', encoding='utf-8')
    file_logger.setLevel(logging.INFO)
    file_logger.setFormatter(formatter)
    
    logger.addHandler(file_logger)
    
    # stream_logger = logging.StreamHandler()
    # stream_logger.setLevel(logging.INFO)
    # stream_logger.setFormatter(formatter)
    
    # logger.addHandler(stream_logger)
    
    return logger

class UserRegistration:

    logger = set_logger()

    def validate_name(self,name):

        pattern=r'[A-Z][a-z]{2,}'

        if re.match(pattern,name):
            self.logger.info("valid name")
            return True
        else:
            self.logger.error("Invalid name")
            return False
            
        
    def validate_email(self,email):
        email_pattern=re.compile("[^0-9][a-z0-9\\-\\+]+[.a-z0-9]@[a-z0-9]+.[a-z]+[.in]")
        email_valid=email_pattern.match(email)

        if email_valid:
            print("the email is valid")
            self.logger.info("the eamil is valid: %s",email)
            return True
        else:
            print("the email is not valid")
            self.logger.error("the eamil is invalid: %s",email)
            raise ValueError("invalid eamil input")

    def validate_ph_number(self,phn_num):

        phn_num_pattern=re.compile('^91 \\d{10}$')
        phn_num_valid=phn_num_pattern.match(phn_num)

        if phn_num_valid:
            print("the number is valid")
            self.logger.info("the number is valid: %s",phn_num)
            return True
        else:

            print("the number is not valid")
            self.logger.error("the number is invalid: %s",phn_num)

            raise ValueError("Invalid input")
        

    def validate_password(self,password):

        password_pattern = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@#?$])[A-Za-z\\d@#?$]{8,}$')
        paswordvalid=password_pattern.match(password)
        if paswordvalid:
            print("passowrd id valid")
            self.logger.info("pasword is valid: %s",password)
            return True
        else:
            print("password is invalid")
            self.logger.error("password is invalid: %s",password)
            raise ValueError("invalid input")

if __name__ == '__main__':       
    
    try:
        user=UserRegistration()

        first_name=input("enter the first name :")
        last_name=input("enter the last name :")

        if user.validate_name(first_name):
            print("the first name is valid")
        else:
            print("the first name is not valid")
            raise ValueError("invalid first name")
        
        if user.validate_name (last_name):
            print("the last name is valid")
        else:
            print("the last name is not valid")
            raise ValueError("invalid last name")
        
        email=input("enter the email :")
        user.validate_email(email)

        phn_num=(input("enter the phone number"))
        user.validate_ph_number(phn_num)

        password=(input("enter the password"))
        user.validate_password(password)

    except Exception as e:
        UserRegistration.logger.exception(e)

