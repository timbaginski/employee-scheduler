# the purpose of this class is to encapsulate an employee
# the employee keeps track of its name, occupation, current shifts, and work availability
from shift import Shift
from days import Day


class Employee:

    # initialize me with a name and occupation
    def __init__(self, name: str, occupation: str):
        self.name = name
        self.occupation = occupation
        self.shifts = []
        self.current_hours = 0
        self.min_hours = 0
        self.max_hours = 40
        self.off_days = []
        self.active = False

    # adds new shift to my shifts and returns True if it meets my requirements
    # returns False if the new shift does not meet my requirements
    def add_shift(self, new_shift: Shift, day: Day) -> bool:
        if (new_shift.get_hours() + self.current_hours > self.max_hours or
                day in self.off_days or not
                new_shift.has_occupation(self.occupation)):
            return False

        self.shifts.append(new_shift)
        new_shift.occupy()
        self.current_hours += new_shift.get_hours()
        return True

    # returns True if I am working enough hours this week, False otherwise
    def is_satisfied(self) -> bool:
        return self.current_hours > self.min_hours

    # returns whether or not I am active
    def is_active(self) -> bool:
        return self.active

    # sets my activity to inactive
    def set_inactive(self):
        self.active = False

    # sets my activity to active
    def set_active(self):
        self.active = True


