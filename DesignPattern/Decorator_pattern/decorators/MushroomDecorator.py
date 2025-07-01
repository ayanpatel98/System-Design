from BasePizza import BasePizza
from decorators.ToppingsDecorator import ToppingsDecorator

class MushroomDecorator(ToppingsDecorator):
    def __init__(self, basePizzaObj: BasePizza):
        self.basePizzaObj = basePizzaObj
    
    def cost(self):
        return self.basePizzaObj.cost()+20