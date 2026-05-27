k=4
l=[1,2,3,4,5]
for i in range(k):
    x=l.pop()     # Remove the last element and store it in x
    l.insert(0,x) # Insert x at the beginning of the list
print(l)