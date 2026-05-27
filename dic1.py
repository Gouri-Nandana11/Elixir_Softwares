d={"1":"one","2":"two","3":"three"}
print(d)

# access values
print(d["1"])

# add new key-value pair
d["4"]="four"
print(d)

# update a value
d.update({"2":"TWO"})
print(d)

# pop a key
d.pop("3")
print(d)

#print all keys
print(d.keys())

#print all values
print(d.values())

#get all values 
print(d.get("1"))

#copy a dictionary
d2=d.copy()
print(d2)

#clear a dictionary
d2.clear()
print(d2)