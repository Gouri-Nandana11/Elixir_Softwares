class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal speaks")
class dog(animal):
    def speak(self):
        print("Dog barks")
a1=animal("Generic Animal")
a1.speak()
d1=dog("Buddy")
d1.speak()