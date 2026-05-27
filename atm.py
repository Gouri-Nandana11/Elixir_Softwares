bal=int(input("enetr the the balance"))
withdraw=int(input("enter the amount to withdrw"))
if bal>withdraw:
    print("new balnce after withdrwal:",bal-withdraw)
    bal-=withdraw
else:
    print("no sufficient balnce")