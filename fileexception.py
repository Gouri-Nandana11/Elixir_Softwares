try:
 f=open('file.txt')
 print(f.read())
except FileNotFoundError:
    print("File not found, please check the file name and try again")