from RoomType import RoomType
from datetime import date

class Room:

    def __init__(self, roomNumber: int, roomType: RoomType):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.bookingSet = set() # (start, end)
    
    def isAvailable(self, startTime: date, endTime: date):
        for start, end in self.bookingSet:
            if not (startTime>=end or endTime<=start):
                return False
        return True
    
    def addBooking(self, startTime: date, endTime: date):
        self.bookingSet.add((startTime, endTime))
    
    def removeBooking(self, startTime: date, endTime: date):
        self.bookingSet.remove((startTime, endTime))
        