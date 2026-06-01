class PasswordException(Exception):
    pass

def check_password(pwd):
    if len(pwd)<8:
        raise PasswordException("Password must be at least 8 characters long")
    else:
        print("Password is valid")
pwd=input("enter password:")
try:
    check_password(pwd)
except PasswordException as e:
    print(e)
