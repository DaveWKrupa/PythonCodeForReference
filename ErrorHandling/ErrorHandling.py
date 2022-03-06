#Error handling
from ValueTooHighError import ValueTooHighError, ValueTooSmallError

# type error
# a = 5 + "mystring"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# file not found error
# f = open('nonexistentfile.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistentfile.txt'


a = [1, 2, 3]
# value error
# when argument is right type but value is wrong
# c = a.remove(4)
# ValueError: list.remove(x): x not in list

# index error
# c = a[4]  # no index 4 so will throw error
# IndexError: list index out of range

# key error
my_dict = {'name': 'Fred'}
# age = my_dict['age']
# KeyError: 'age'


# raise a custom exception
# x = -5
# if x < 0:
#     raise Exception('x should be positive')
# Exception: x should be positive

# assert statement
# will raise an assertion error if the expression returns false
x = -5
# assert(x >= 0), 'x should be positive'
# AssertionError: x should be positive


# try/catch
# zerodivisionerror
# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)
# division by zero

# specify the type of error, and include an else and a finally clause
# try:
#     a = 5 / 0
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("no exception happened")
# finally:
#     print("this runs regardless of whether an error happened or not")
# division by zero

# using the custom ValueTooHighError


def test_value(testvalue):
    if testvalue > 100:
        raise ValueTooHighError("Value is too high")
    if testvalue < 5:
        raise ValueTooSmallError("Value too small", testvalue)


# try:
#     test_value(101)
# except ValueTooHighError as e:
#     print(e)
# Value is too high

# try:
#     test_value(3)
# except ValueTooSmallError as e:
#     print(e.message)
#     print(e.value)
# Value too small
# 3