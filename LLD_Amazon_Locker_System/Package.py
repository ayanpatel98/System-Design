from LockerSize import LockerSize

class Package:
    def __init__(self, id: int, size: LockerSize):
        self.id: int = id
        self.size: LockerSize = size