str1=input("enter your  name:")
str2=int(input("enter the password:"))
if len(str1)<=1:
    print("enter the valid name")
elif str2<=4:
    print("enter the valid password")
else:
    print("login successful")