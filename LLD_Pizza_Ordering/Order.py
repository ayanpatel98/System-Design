from Pizza import Pizza
from PizzaToppings import PizzaToppings
from OrderStatus import OrderStatus

class Order:

    def __init__(self, id: int, pizza: Pizza):
        self.id = id
        self.pizza = pizza
        self.orderStatus = OrderStatus.PENDING