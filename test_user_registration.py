from  user_registration import UserRegistration
import pytest

@pytest.fixture
def user():
    return UserRegistration()


def test_validate_name(user):
    assert user.validate_name("Aditya")==True

def test_validate_name_failure(user):
    assert user.validate_name("singh")==False
    

def test_validate_email(user):
    assert user.validate_email("adityasinghi12@gmail.com")==True

def test_validate_email_failure(user):
    with pytest.raises(ValueError):
        assert user.validate_email("singh@1")

def test_validate_phn_number(user):
    assert user.validate_ph_number("91 8969745425")==True

def test_validate_phn_number_failure(user):
    with pytest.raises(ValueError):
        assert user.validate_ph_number("8969745425")
    
    
def test_validate_passwprd(user):
   assert user.validate_password("Ironman@123")==True
def test_validate_passwprd_failure(user):
   with pytest.raises(ValueError):
    assert user.validate_password("ronman@123")