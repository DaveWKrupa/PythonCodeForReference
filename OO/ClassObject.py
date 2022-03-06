from Student import Student
from CookingStudent import CookingStudent
from Car import Car

student1 = Student("Bill", "123 Fake St", "888.888.8888", 2.3, "Photography", False)

print(student1.phone)

student1.phone = "999.999.9999"
print(student1.phone)
print(student1.gpa)
print(student1.on_honor_roll())

cookingstudent1 = CookingStudent("broccoli")
cookingstudent1.name = "John"
cookingstudent1.address = "345 Street Blvd"
cookingstudent1.phone = "999.999.9999"
cookingstudent1.gpa = 1.6
cookingstudent1.is_on_probation = True
print(cookingstudent1.special_dish)
print(cookingstudent1.name)

car1 = Car()
car1.color = "red"
car1.make = "Dodge"
car1.model = "Dakota"
car1.year = 2001

print(car1.color)
