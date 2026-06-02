class BankAcc:
    def __init__(self,accno,name,balance):
        self.__accno=accno
        self.name=name
        self.__balance=balance
    def getacc(self):
        return self.__accno
    def showbalnce(self):
        return self.__balance
    def depo(self,amt):
        self.__balance+=amt
        print(amt)
    def withdraw(self,w):
        self.__balance-=w
        print(w)
bc=BankAcc(1,'goury',3000)
print("accno:",bc.getacc(),"name:",bc.name)
bc.showbalnce()
bc.depo(3000)
bc.withdraw(30)
