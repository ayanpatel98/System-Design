'''
functional:
- user orders the pizza from the options of pizzas available
- system takes the order, and takes the payment and updates the order

entities:
enums: PizzaSize, PizzaCrust, PizzaToppings, OrderStatus
Pizza: size, crust, list of toppings
PizzaBuilder: setCrust, setSize, addToppings, build
Order: orderID, orderStatus, calculateTotal (base pizza+toppings) | can lave a list of pizzas
OrderService: takes the order, makes the payment and updates the status
'''

from Order import Order
from Pizza import Pizza
from PizzaBuilder import PizzaBuilder
from OrderingService import OrderingSevice
from PizzaSize import PizzaSize
from PizzaCrust import PizzaCrust
from PizzaToppings import PizzaToppings

builder = PizzaBuilder()

pizza = builder.setCrust(PizzaCrust.BROOKLYN).setSize(PizzaSize.LARGE).addToppings(PizzaToppings.JALEPENOS).addToppings(PizzaToppings.OLIVES).build()

orderService = OrderingSevice()

order = orderService.addOrder(pizza)
orderService.calculatePrice(order)
