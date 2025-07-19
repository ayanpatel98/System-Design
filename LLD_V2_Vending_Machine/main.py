'''
vending machine:
Functional:
vending machine states:
Idle State: pressInsertButton
Accept Money: insertMoney, cancel/refund, selectProductButton
Choose Product: cancel/refund, insertProductCode
Dispense state: dispense

entities:
enum: ItemType
Item: id, ItemType, price 
ItemShelf: code, Item
Inventory: list of item Shelf
VendingMachine: inventory, State, availableMoney

'''