# the purpose of this class is to encapsulate an employee
# the employee keeps track of its name, occupation, current shifts, and work availability
from shift import Shift


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

    # adds new shift to my shifts and returns True if it meets my requirements
    # returns False if the new shift does not meet my requirements
    def add_shift(self, new_shift: Shift) -> bool:
        if (new_shift.get_hours() + self.current_hours > self.max_hours or
                new_shift.is_on_off_day(self.off_days) or not
                new_shift.has_occupation(self.occupation)):
            return False

        self.shifts.append(new_shift)
        new_shift.occupy()
        self.current_hours += new_shift.get_hours()
        return True


