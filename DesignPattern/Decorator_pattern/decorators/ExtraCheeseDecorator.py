from decorators.ToppingsDecorator import ToppingsDecorator
from BasePizza import BasePizza

class ExtraCheeseDecorator(ToppingsDecorator):
    def __init__(self, basePizzaObj: BasePizza):
        self.basePizzaObj = basePizzaObj
    
    def cost(self):
        return self.basePizzaObj.cost()+10