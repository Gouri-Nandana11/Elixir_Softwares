num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print(num1,"is greater than",num2)
elif num1<num2:
    print(num2,"is greater than",num1)
else:
    print("both numbers are equal")

#largest of three numbers
num1=int(input("enter first number: "))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number"))
if num2>num1 and num2>num3:
     print("largest:",num2)
elif num3>num1:
    print("largest:",num3)
else:
    print(num1)

#check if divisible by 3 and 5
num1=15
if num1%5 ==0 and num1%3==0:
    print("divisible")
else :
    print("not")