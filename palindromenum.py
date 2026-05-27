inp=input("enter number or string")
if inp.isalpha():
    if inp==inp[::-1]:
        print(inp,"is a palindrome")
    else:
        print(inp,"is not a palindrome")
elif inp.isdigit():
    if inp==inp[::-1]:
        print(inp,"is a palindrome")
    else:
        print(inp,"is not a palindrome")
else:
    print("invalid input")