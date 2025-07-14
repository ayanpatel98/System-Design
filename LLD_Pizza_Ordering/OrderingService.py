from Order import Order
from Pizza import Pizza
from OrderStatus import OrderStatus
import collections

class OrderingSevice:
    
    def __init__(self):
        self.orderList: dict[int, Order] = collections.defaultdict(Order)
    
    def addOrder(self, pizzaSelection: Pizza):
        newOrder = Order(len(self.orderList)+1, pizzaSelection)

        self.orderList[len(self.orderList)+1] = newOrder
        print("Your OrderId: ", newOrder.id)
        return newOrder
    
    def getOrderStatus(self, order: Order):
        print("Your Order Status: ", order.orderStatus)
        return order.orderStatus
    
    def calculatePrice(self, order: Order):
        total = 0
        for topping in order.pizza.toppings:
            total+=topping.value[0]
        
        print("Your Order Total: ", total + order.pizza.size.value[0])
        return total+ order.pizza.size.value[0]
    
    def makePayment(self, order: Order):
        print("Processing your Order")
        self.orderList[order.id] = OrderStatus.COMPLETED
        
        print("Payment Completed")
    