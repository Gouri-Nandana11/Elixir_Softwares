#create a set
set1={1, 2, 3, 4, 5}
print(set1)

# add an element to the set
set1.add(6)
print(set1)

#remove element using remuve
set1.remove(6)
print(set1)

#remove element using discard
set1.discard(5)
print(set1)

#union of two sets
set2={4, 5, 6, 7, 8}
unionset=set1.union(set2)
print(unionset)

#intersection of two sets
intersectionset=set1.intersection(set2)
print(intersectionset)

#difference of two sets
difset=set1.difference(set2)
print(difset)

# check length of set
print(len(set1))

#convert list to set
lst=[1, 2, 3, 4, 5]
set3=set(lst)
print(set3)

#clear aa set
set3.clear()
print(set3)
