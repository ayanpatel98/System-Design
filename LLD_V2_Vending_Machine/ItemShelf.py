from Item import Item

class ItemShelf:
    def __init__(self, code: int, item: Item):
        self.code = code
        self.item = item
        self.issoldOut = False
        