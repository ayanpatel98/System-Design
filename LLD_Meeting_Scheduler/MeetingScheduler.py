from Meeting import Meeting
from MeetingRoom import MeetingRoom
import random

class MeetingScheduler:

    def __init__(self, meetingRooms: int):
        self.meetingRooms: list[MeetingRoom] = [MeetingRoom(i, random.randint(1, 2), True) for i in range(meetingRooms)]

    def getAvailableMeetingRoom(self, meeting: Meeting):
        for meetingRoom in self.meetingRooms:
            if len(meeting.people)<=meetingRoom.capacity and meetingRoom.isAvailable:
                print(meetingRoom.id)
                return meetingRoom
        return None

    def bookMeetingRoom(self, meeting: Meeting):
        availableMeetingRoom  = self.getAvailableMeetingRoom(meeting)
        if not availableMeetingRoom:
            print("Meeting Room not available")
            return
        
        availableMeetingRoom.isAvailable = False

        self.notifyPeople(meeting)
        print("Meeting Booked in meeting room: ", availableMeetingRoom.id)

    def notifyPeople(self, meeting: Meeting):
        for person in meeting.people:
            print(person.name, " with email ", person.email, " notified")
