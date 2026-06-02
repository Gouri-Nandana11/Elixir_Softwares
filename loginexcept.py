class LoginException(Exception):
    pass
try:
    user=input("Enter username: ")
    pwd=input("Enter password: ")
    if user!="admin" or pwd!="123":
        raise LoginException("Invalid username or password")
    else:
        print("Login successful")
except LoginException as e:
    print(e)