from Room import Room
from datetime import date
from BookingStatus import BookingStatus

class Booking:

    def __init__(self, id: int, name: str, room: Room, startTime: date, endTime: date):
        self.id = id
        self.room = room
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.bookingStatus = BookingStatus.BOOKED