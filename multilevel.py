class A:
    def display(self):
        print('display a')
class b(A):
    def displayb(self):
        print("b")
class c(b):
    def displayc(self):
        print("c")
c1=c()
c1.display()
c1.displayb()
c1.displayc()