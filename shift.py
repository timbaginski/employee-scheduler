# this class encapsulates a shift
# the shift has a start and end time, as well as an occupation for the employee that will fill it
from days import Day


class Shift:

    # initialize me with a start_time, end_time, and required occupation
    def __init__(self, start_time: float, end_time: float, occupation: str, day: Day):
        self.start_time = start_time
        self.end_time = end_time
        self.occupation = occupation
        self.occupied = False
        self.day = day

    # returns the number of hours I take
    def get_hours(self) -> float:
        return self.start_time - self.end_time

    # returns my occupation
    def get_occupation(self):
        return self.occupation

    # returns bool representing whether or not I fall on an employees off day
    def is_on_off_day(self, off_days: list) -> bool:
        return self.day in off_days

    # returns whether my occupation matches an employee's occupation
    def has_occupation(self, occupation: str) -> bool:
        return self.occupation == occupation

    # occupies me by setting occupied to true
    def occupy(self):
        self.occupied = True

