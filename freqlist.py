l1=["1","2","3","1","2"]
d={}
for i in l1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)