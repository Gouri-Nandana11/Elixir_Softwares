list1=[1,2,3]
list2=[4,5,1]


#create dictionary from list
d={}
i=0
while i<len(list1):
    d[list1[i]]=list2[i]
    i+=1
print(d)

#common elem of two list1
for i in list1:
    for j in list2:
        if i==j:
             print(i)
