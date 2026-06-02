class student:
  def __init__(self,roll,name):
    self.__roll=roll
    self.name=name
  def getRoll(self):
     return self.__roll
s=student(2,"raji")
print("roll:",s.getRoll())
print(s.name)
