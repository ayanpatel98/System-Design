from Meeting import Meeting
from Person import Person
from Meeting import Meeting
from MeetingScheduler import MeetingScheduler

'''
functional req:
- user should be able to schedule the meeting
- there are n meeting rooms with capacity
- every meeting has start end time and number of people
- send notifications to all the people when the meeting is scheduled

entities:
- Meeting (id, start time, end time, list of People)
- Person (id, name, email)
- MeetingRoom (id, capacity, isAvailable)
- MeetingScheduler (list of MeetingRooms, isMeetingRoomAvailable(capacity), bookMeeting, notifyPeople)
'''

if __name__=="__main__":
    p1, p2 = Person(1, "Ayan", "ayan@gmail.com"), Person(2, "Patel", "patel@gmail.com")
    p3, p4 = Person(3, "a1", "ayan@gmail.com"), Person(4, "p1", "patel@gmail.com")

    meeting1 = Meeting(101, 1, 3, [p1, p2])
    meeting2 = Meeting(102, 2, 4, [p3, p4])

    scheduler = MeetingScheduler(2)

    # scheduler.bookMeetingRoom(meeting1)
    scheduler.bookMeetingRoom(meeting1)
    scheduler.bookMeetingRoom(meeting2)
    scheduler.getAvailableMeetingRoom(meeting1)