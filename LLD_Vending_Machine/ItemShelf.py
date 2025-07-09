from Item import Item

class ItemShelf:

    def __init__(self, itemCode: int, item: Item):
        self.item = item
        self.itemCode = itemCode
        self.isSoldOut = False