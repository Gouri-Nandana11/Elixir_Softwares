str="abc@2004"
d=[]
for i in str:
    if i.isalpha():
        d.append(i)
print("".join(d))