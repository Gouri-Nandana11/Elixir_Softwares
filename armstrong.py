num=input("enter the number: ")
l=len(num)
sum=0
for i in num:
    sum+=int(i)**l
if sum==int(num):
    print("armstrong number")