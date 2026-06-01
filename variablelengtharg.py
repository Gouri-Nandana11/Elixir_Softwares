def sums(*num):
    suma=0
    print(sum(num))
sums(3,3,6,9)

#all given names
def names(*name):
    print(name)
names('akku','mikku','kuku')

#findlargest number using args
def large(*num):
    largest=num[0]
    for i in num:
        if i>largest:
            largest=i
    print(largest)
large(2,4,7)

#average of numbers
def avgo(*num):
    sums=0
    for i in num:
        sums+=i
    avgn=sums/(len(num))
    print(avgn)
avgo(2,2)

#customer info dynamic
def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(name="aash",age=5)


        
