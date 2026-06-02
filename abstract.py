from abc import ABC,abstractmethod 
class shape:
    @abstractmethod
    def area(self):
        pass
class sqr(shape):
    def __init__(self,s):
        self.side=s
    def area(self):
        return self.side**2
s=sqr(2)
print("area:",s.area())
        