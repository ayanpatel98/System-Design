from Person import Person

class Meeting:
    def __init__(self, id: int, start: int, end: int, people: list[Person]):
        self.id = id
        self.start = start
        self.end = end
        self.people = people