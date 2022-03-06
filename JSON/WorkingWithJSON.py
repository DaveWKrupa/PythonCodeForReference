import json
from Student import Student
# serializing, deserializing
# converting a dictionary object to its JSON equivalent

person = {"name": "Dave", "age": 43, "city": "Seattle", "trueorfalse": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4)
# print(personJSON)
# {
#     "name": "Dave",
#     "age": 43,
#     "city": "Seattle",
#     "trueorfalse": false,
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }

# sort keys alphabetically
# the s in dumps stands for string, as in "dump to string"
personJSONSorted = json.dumps(person, indent=4, sort_keys=True)
# print(personJSONSorted)
# {
#     "age": 43,
#     "city": "Seattle",
#     "name": "Dave",
#     "titles": [
#         "engineer",
#         "programmer"
#     ],
#     "trueorfalse": false
# }

# now dump it to a file
# note that dump does not have the s when going to a file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# now load the json into a Python dictionary object from a string
# the difference in this example between JSON and python dictionary is that False is capitalized in dictionary
personDict = json.loads(personJSON)
# print(personDict)
#  {'name': 'Dave', 'age': 43, 'city': 'Seattle', 'trueorfalse': False, 'titles': ['engineer', 'programmer']}

with open('widget.json', 'r') as file:
    widget = json.load(file)

# print(widget)
# {'widget': {'debug': 'on', 'window': {'title': 'Sample Konfabulator Widget', 'name': 'main_window', 'width': 500, 'height': 500}, 'image': {'src': 'Images/Sun.png', 'name': 'sun1', 'hOffset': 250, 'vOffset': 250, 'alignment': 'center'}, 'text': {'data': 'Click Here', 'size': 36, 'style': 'bold', 'name': 'text1', 'hOffset': 250, 'vOffset': 100, 'alignment': 'center', 'onMouseUp': 'sun1.opacity = (sun1.opacity / 100) * 90;'}}}


# encoding a custom object and writing it to a string

student = Student("Joe", "123 Fake St", "333.333.3333", 3.7, "Accounting", False)

def encode_student(o):
    if isinstance(o, Student):
        return {'name': o.name, 'address': o.address, 'phone': o.phone, 'gpa': o.gpa,
                'major': o.major, 'is_on_probation': o.is_on_probation}
    else:
        raise TypeError('Object is type Student.')


studentJson = json.dumps(student, default=encode_student)
# print(studentJson)
# {"name": "Joe", "address": "123 Fake St", "phone": "333.333.3333", "gpa": 3.7, "major": "Accounting", "is_on_probation": false}


# load the studentJson string into student object
# no easy way to do this, just have to set that values from the passed in dictionary
def decode_student(dct):
    return Student(name=dct["name"], address=dct["address"], phone=dct["phone"], gpa=dct["gpa"],
                   major=dct["major"], is_on_probation=dct["is_on_probation"])


student = json.loads(studentJson, object_hook=decode_student)
print(student.name)
# Joe