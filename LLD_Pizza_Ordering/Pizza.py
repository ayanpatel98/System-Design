from PizzaSize import PizzaSize
from PizzaCrust import PizzaCrust
from PizzaToppings import PizzaToppings

class Pizza:
    def __init__(self, pizzaBuilder):
        self.size: PizzaSize = pizzaBuilder.size
        self.crust: PizzaCrust = pizzaBuilder.crust
        self.toppings: list[PizzaToppings] = pizzaBuilder.toppings