'''
Hotel Management system

functional:
- can search, book or cancel rooms, get booking details when room is booked
- room has availability

entities:
enums: RoomType, BookingStatus
Room: roomNumber, RoomType, set of bookedTimes, isAvailable(startTime, endTime), addBooking(start, endTime), removeBooking(start, endTime)
Booking: id, room, name, startTime, endTime, BookingStatus
BookingSystem: map of rooms, bookings map, addRoom(), searchRoom(roomType, startTime, endTime), 
               bookRoom(roomNumber, name, startTime, EndTime), cancelBooking(bookingNumber)
'''

from Room import Room
from Booking import Booking
from BookingSystem import BookingSystem
from RoomType import RoomType
from datetime import date, timedelta

room1 = Room(1, RoomType.DOUBLE)
room2 = Room(2, RoomType.DOUBLE)
room3 = Room(3, RoomType.SINGLE)

bookingSystem = BookingSystem()

bookingSystem.addRoom(room1)
bookingSystem.addRoom(room2)
bookingSystem.addRoom(room3)
print(bookingSystem.roomsMap)

bookingSystem.searchRoom(RoomType.DOUBLE, date(2025,8,1),  date(2025,8,1))