a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
while True:
 print("1.Add 2.sub 3.mul 4.exit")
 choice=int(input("enter the choice"))
 if choice == 1:
    print("addition: ",a+b)
 elif choice==2:
    print("substraction :",a-b)
 elif choice==3:
    print("mul: ",a*b)
 elif choice==4:
    exit
 else:
    print("..invslid case")

