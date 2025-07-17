from Room import Room
from Booking import Booking
from datetime import date
from RoomType import RoomType
from BookingStatus import BookingStatus

class BookingSystem:

    def __init__(self):
        self.roomsMap: dict[int, Room] = {}
        self.bookingsMap: dict[int, Booking] = {}
    
    def addRoom(self, room: Room):
        self.roomsMap[room.roomNumber] = room
        print("room added")
    
    def searchRoom(self, roomType: RoomType, startTime: date, endTime: date):
        for room in self.roomsMap.values():
            if room.roomType==roomType and room.isAvailable(startTime, endTime):
                return room
        print("Room not Available")
        return None
    
    def bookRoom(self, roomNumber: int, name: str, startTime: date, endTime: date):
        if roomNumber not in self.roomsMap:
            print("invalid room")
            return None

        room = self.roomsMap[roomNumber]

        if not room.isAvailable(startTime, endTime):
            print("room is not available")
            return None
        
        room.addBooking(startTime, endTime)
        booking = Booking(len(self.bookingsMap), name, room, startTime, endTime)
        self.bookingsMap[len(self.bookingsMap)] = booking

        print("room booked")
        return booking
    
    def cancelBooking(self, bookingNumber: int):
        if bookingNumber not in self.bookingsMap:
            print("booking does not exist")
            return
        
        booking = self.bookingsMap[bookingNumber]
        booking.bookingStatus = BookingStatus.CANCELLED
        booking.room.removeBooking(booking.startTime, booking.endTime)
        print("booking cancelled")
        return
