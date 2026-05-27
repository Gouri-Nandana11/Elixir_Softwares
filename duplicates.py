def duplicate():
    str1="banana"
  
    d=[]
    for i in str1:
       if i not in d:
              d.append(i)
    print(d)

duplicate()
