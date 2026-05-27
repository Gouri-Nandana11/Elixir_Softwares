lst = [1, 2, 3, 4, 5]

k = 2

for i in range(k):
    x = lst.pop()     
    lst.insert(0, x)   

print(lst)