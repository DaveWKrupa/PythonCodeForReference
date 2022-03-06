# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# deque Deque (Doubly Ended Queue)
# Deque is preferred over a list in the cases where we need quicker
# append and pop operations from both the ends of the container
d = deque()
d.append(1)
d.append(2)
d.append(3)
# print(list(d))
# deque([1, 2, 3])

# print(list(d))
# [1, 2, 3]

d.appendleft(9)
# print(list(d))
# [9, 1, 2, 3]

d.pop()
# print(list(d))
# [9, 1, 2]

d.popleft()
# print(list(d))
# [1, 2]

d.clear()
# print(list(d))
# []

d.append(14)
d.extend([10, 11, 12])
# print(list(d))
# [14, 10, 11, 12]

d.extendleft([1011, 1111, 1211])  #will reverse these numbers while adding
# print(list(d))
# [1211, 1111, 1011, 14, 10, 11, 12]

d.rotate()
# print(list(d))
# [12, 1211, 1111, 1011, 14, 10, 11]

d.rotate()
# print(list(d))
# [11, 12, 1211, 1111, 1011, 14, 10]

d.rotate(-1)
# print(list(d))
# [12, 1211, 1111, 1011, 14, 10, 11]



# defaultdict dictionary that has default values
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
# print(d['c'])  # this would raise a key error with a regular dictionary but a 0 with this one
# 0

# for older versions of Python you use OrderedDict to create a dictionary that remembers the
# order items are added.
# The latest Python the dictionary does that
myOrderedDict = OrderedDict()

#  namedtuple creates an immutable struct

point = namedtuple('Point', 'x,y,z')
pt = point(2, -3, 5)
# print(pt.x)
# print(pt.y)
# print(pt.z)
# 2
# -3
# 5

# pt.x = 9
# AttributeError: can't set attribute



# it is possible to create an immutable structure with a mutable value
Person = namedtuple("Person", "name children")
john = Person("John Doe", ["Timmy", "Jimmy"])
# print(john)
# Person(name='John Doe', children=['Timmy', 'Jimmy'])
john.children.append("Tina")
# print(john)
# Person(name='John Doe', children=['Timmy', 'Jimmy', 'Tina'])




# the Counter object takes a list or string and creates
# a dictionary, where the key is a unique item in the list
# and the value is the count of that item

# astring = "abdbdbaabdbabbdbabdbaabdbabdddbdbddhhdhhdrrrwbbsii"  # any iterable datatype
# my_counter = Counter(astring)
# print(my_counter)
# print(my_counter.most_common())  # returns a list of tuples with all the items in order of most to least common
# print(my_counter.most_common(2))  # returns list of the top 2
# print(my_counter.most_common(1))  # returns a list with only the top tuple in it
# print(my_counter.most_common(1)[0])  # returns the first tuple in the list containing just the one tuple
# print(my_counter.most_common(1)[0][0])  # returns the first item in the first tuple in the list
# print(list(my_counter.elements()))  # get a list of the elements in my_counter
#
# listofstuff = ["gf", "hi", "dr", "hi", "sc", "po", "sc", "fd", "df", "gf", "df", "po", "po", "fd", "gf", "sc", "sc"]
# my_counter = Counter(listofstuff)
# print(my_counter)
# for key, value in my_counter.items():
#    print(key)
#    print(value)


