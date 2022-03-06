class Student:
    def __init__(self, name, address, phone, gpa, major, is_on_probation):
        self.name = name
        self.address = address
        self.phone = phone
        self.gpa = gpa
        self.major = major
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        