from ItemType import ItemType

class Item:

    def __init__(self, itemType: ItemType, price: int):
        self.itemType = itemType
        self.price = price