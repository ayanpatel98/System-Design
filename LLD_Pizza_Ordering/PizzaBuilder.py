from PizzaSize import PizzaSize
from PizzaCrust import PizzaCrust
from PizzaToppings import PizzaToppings
from Pizza import Pizza

class PizzaBuilder:

    def __init__(self):
        self.size: PizzaSize = None
        self.crust: PizzaCrust = None
        self.toppings: list[PizzaToppings] = []
    
    def setSize(self, size: PizzaSize):
        self.size = size
        return self
    
    def setCrust(self, crust: PizzaCrust):
        self.crust = crust
        return self
    
    def addToppings(self, topping: PizzaToppings):
        self.toppings.append(topping)
        return self
    
    def build(self):
        return Pizza(self)