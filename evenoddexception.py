num1=int(input())
try:
    if num1%2==0:
        raise Exception("Even number exception")
    else:
        print("Odd number")
except Exception as e:
    print(e)