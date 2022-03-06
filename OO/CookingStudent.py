from Student import Student
# this is the syntax for inheritance


class CookingStudent(Student):
    def __init__(self, special_dish):
        self.special_dish = special_dish
