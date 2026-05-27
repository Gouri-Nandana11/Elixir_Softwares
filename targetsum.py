target=10
l=[2,3,5,7,11]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j]==target:
            print(l[i],l[j])