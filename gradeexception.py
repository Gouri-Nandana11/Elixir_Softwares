mark=int(input())
try:
    if mark >=90:
        print("Grade A")
    elif mark >=80:
        print("Grade B")
    elif mark >=70:
        print("Grade C")
    elif mark >=60:
        print("Grade D")
    else:
        print("Grade F")
except ValueError:
    print("Invalid input, please enter a number")
