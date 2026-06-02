f=open("abc.txt","a")
f.write("\nthis is to append to the file")
f.close()
with open("abc.txt", "r") as f:
    line = f.readline()
    while line != "":
        print(line.strip())
        line = f.readline()
        
with open("abc.txt", "r+") as f:
    content = f.read()
    print("Current content of the file:")
    print(content)
    f.seek(0)
    f.write("This is the new content of the file.\n")
    f.write(content)
    print(f.tell())

