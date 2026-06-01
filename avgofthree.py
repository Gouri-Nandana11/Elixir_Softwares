a=int(input())
b=int(input())
c=int(input())
try:
    if a<0 or b<0 or c<0:
        raise Exception("Negative number exception")
    else:
        avg=(a+b+c)/3
        print(avg)
except Exception as e:
    print(e)