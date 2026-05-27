str1="ef"
if len(str1)==0:
    print("string is empty")
else:
    print("string is not empty")

#start with vowel
str="apple"
v="aeiouAEIOU"
if str[0] in v:
    print("string starts with vowel")
else:
    print("string does not start with vowel")

#check if string is equal
str1="hello"
str2="hello"
if str1==str2:
    print("strings are equal")  
else:
    print("strings are not equal")

#upper
str="hello"
if str.isupper():
    print("string is in uppercase")
else:
    print("string is not in uppercase")
#check if chara or not
char='a'
if char.isalpha():
    print("character is a letter")
else:
    print("character is not a letter")