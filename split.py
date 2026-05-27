str1="this is aashi"
str2=str1.split()
counter=0
for i in str2:
    counter+=1
print(counter)

print(max(str2,key=len))