from ItemShelf import ItemShelf
from ItemType import ItemType
from Item import Item

class Inventory:

    def __init__(self):
        self.shelfList: list[ItemShelf] = []
        self.initializeInventory()
    
    def initializeInventory(self):
        for i in range(10):
            item = None
            if i>0 and i<3:
                item = Item(i, ItemType.COKE, 10)
            elif i>3 and i<6:
                item = Item(i, ItemType.PEPSI, 20)
            elif i>6 and i<10:
                item = Item(i, ItemType.SODA, 30)

            self.shelfList.append(item)

    def addShelf(self, itemShelf: ItemShelf):
        self.shelfList.append(itemShelf)