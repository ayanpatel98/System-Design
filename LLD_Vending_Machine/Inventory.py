from ItemShelf import ItemShelf
from Item import Item
from ItemType import ItemType

class Inventory:

    def __init__(self, noOfShelf: int):
        self.noOfShelf = noOfShelf
        self.shelf: list[ItemShelf] = []
        self.initializeShelfs()

    def initializeShelfs(self):
        for i in range(self.noOfShelf):
            item = Item()
            if i<3:
                item.itemType = ItemType.JUICE
                item.price = 15
            elif i<6:
                item.itemType = ItemType.PEPSI
                item.price = 10
            elif i<10:
                item.itemType = ItemType.SODA
                item.price = 5

            self.shelf.append(ItemShelf(i+1, item))
    
    def removeFromInvetory(self, itemCode: int):
        for item in self.shelf:
            if item.isSolfOut:
                return False
            item.isSoldOut = True
            return True
    
    def updateInventory(self, price, itemType: ItemType):
        self.shelf.append(ItemShelf(len(self.shelf), Item(itemType, price)))
    
    def getProduct(self, code: int):
        for shelf in self.shelf:
            if shelf.itemCode==code:
                return shelf
        return None