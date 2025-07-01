from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self):
        print("I am in parent constructor")
    
    def roadSky(self):
        print("I am in a parent method")
    
    def start(self):
        print('Parent Starting')
    
    @abstractmethod
    def abstractMethod(self):
        pass

class Child(Vehicle):
    static_var = 3
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("I am in a child constructor", Child.static_var)
    
    @staticmethod
    def info():
        print("Inside static method", Child.static_var)

    def road(self):
        print('I am in a child method')

    def start(self):
        print('Child Starting')
    
    def abstractMethod(self):
        print("Abstract Method")
    
    def __add__(self, otherObj):
        a = self.num1+otherObj.num1
        b = self.num2+otherObj.num2
        return Child(a, b)

    def __str__(self):
        return "{} {}".format(self.num1, self.num2)

child = Child(1, 2)
# child2 = Child(2, 3)
# ans = child+child2
Child.info()
