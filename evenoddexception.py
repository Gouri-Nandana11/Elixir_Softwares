<<<<<<< HEAD
num1=int(input())
try:
    if num1%2==0:
        raise Exception("Even number exception")
    else:
        print("Odd number")
except Exception as e:
=======
num1=int(input())
try:
    if num1%2==0:
        raise Exception("Even number exception")
    else:
        print("Odd number")
except Exception as e:
>>>>>>> ef28620f33e45297545b8355437f940478af35b9
    print(e)