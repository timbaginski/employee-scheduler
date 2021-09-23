from employee import Employee
from days import Day
from shift import Shift


class Calender:

    # creates me with empty list of employees
    def __init__(self):
        self.employees = []
        self.shifts = []
        self.days = [] * 7

    # creates a new employee and adds it to my employees list
    def create_employee(self, name: str, occupation: str):
        self.employees.append(Employee(name, occupation))

    # creates a new kind of shift and adds it to the shifts list
    def create_shift(self, start_time: float, end_time: float, occupation: str):
        self.shifts.append([start_time, end_time, occupation])

    # creates a shift from the start_time, end_time, occupation template and adds it to a specific day
    def add_shift(self, i: int, day: Day):
        temp = Shift(self.shifts[i][0], self.shifts[i][1], self.shifts[i][2])
        self.days[day].append(temp)

    # adds employee to a shift on a given day. Returns True if successful, False otherwise
    def schedule_on_day(self, employee: Employee, day: Day):
        for shift in self.days[day]:
            if employee.add_shift(shift, day) and not shift.is_occupied():
                return True

        return False




    
