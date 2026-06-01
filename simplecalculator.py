a=int(input())
b=int(input())
print("1.Add,2.sub,3.divide,4.exit")
while True:
    print("enter your choice")
    try:   
        ch=int(input())
        if ch==1:
            print(a+b)
        elif ch==2:
            print(a-b)
        elif ch==3:
            print(a/b)
        elif ch==4:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input, please enter a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")

