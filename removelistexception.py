list1=[1,2,3,4]
try:
    list1.remove(5)
except ValueError:
    print("Value not found in the list, cannot remove")