l=[1,2,4,7,4]
print(sum(l))
l.sort
print("largest of list :",l[-1])
print("smallest of list :",l[0])
l1=[]
for i in l:
  if i not in l1:
     l1.append(i)
print(l1)

