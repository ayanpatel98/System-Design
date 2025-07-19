from ItemType import ItemType

class Item:
    def __init__(self, id: int, itemType: ItemType, price: int):
        self.id = id
        self.itemType = itemType
        self.price = price
        