from enum import Enum

class FlightStatus(Enum):
    ONTIME = 1,
    DELAYED = 0,
    CANCELLED = -1,