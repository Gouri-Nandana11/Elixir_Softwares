string=input("Enter a string: ")
try:
    num=float(string)
    print("The string can be converted to a float:", num)
except ValueError:
    print("The string cannot be converted to a float.")