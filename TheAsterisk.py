# all the things you can do with the asterisk

# multiply
x = 5 * 4
# print(x)
# 20

# power operation raise to the power of
x = 2 ** 10
# print(x)
# 1024

# create a list with repeated elements
zeros = [0] * 10
# print(zeros)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros_and_ones = [0, 1] * 10
# print(zeros_and_ones)
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# works with tuples
my_tuple = (1, 2, 3) * 10
# print(my_tuple)
# (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
my_string = "ABC" * 10
# print(my_string)
# ABCABCABCABCABCABCABCABCABCABC


# *args and **kwargs
def many_parameters(*args, **kwargs):
    # loop through *args tuple
    for arg in args:
        print(arg)
    # loop through **kwargs dictionary
    for key in kwargs:
        print(key, kwargs[key])


# many_parameters(1, 2, 3, 4, 5, six=6, seven=7, eight=8)
# 1
# 2
# 3
# 4
# 5
# six 6
# seven 7
# eight 8


# When an asterisk is in the list of parameters it forces the caller to use named arguments
# for every parameter after the asterisk
# for example, the following function allows 2 positional arguments and then two named arguments
# note that the asterisk does not add any new parameters, so this only has 4, not 5 parameters

def asterisk_func_one(a, b, *, c, d):
    print(a, b, c, d)


# unpacking arguments is a way to pass an iterable to a function instead of individual values
def foo(a, b, c):
    print(a, b, c)


# use an asterisk next to the list name to unpack it into the argument list
my_list = [9, 8, 7]
# foo(*my_list)
# 9 8 7

my_tuple = (2, 3, 4)
# foo(*my_tuple)
# 2 3 4

# unpacking a dictionary takes two asterisks, and the keys must match the parameter names
# order does not matter since using names
my_dictionary = {"b": 7, "c": 8, "a": 6}
# foo(**my_dictionary)
# 6 7 8

# too many items in the dictionary or mismatched names will result in an error
# my_dictionary = {"b": 7, "c": 8, "a": 6, "d": 9}
# foo(**my_dictionary)
# TypeError: foo() got an unexpected keyword argument 'd'


# an asterisk can be used to unpack lists
# in this example the asterisk before the first return value
# gets numbers 1 through 5
my_list = [1, 2, 3, 4, 5, 6]
*everything_but_the_last_number, the_last_number = my_list
# print(everything_but_the_last_number)
# print(the_last_number)
# [1, 2, 3, 4, 5]
# 6

*everything_but_the_last_two_numbers, the_second_to_the_last_number, the_last_number = my_list

# print(everything_but_the_last_two_numbers)
# print(the_second_to_the_last_number)
# print(the_last_number)
# [1, 2, 3, 4]
# 5
# 6

the_first_number, *everything_in_the_middle, the_last_number = my_list
# print(the_first_number)
# print(everything_in_the_middle)
# print(the_last_number)
# 1
# [2, 3, 4, 5]
# 6

the_first_number, *the_rest_of_the_numbers = my_list
# print(the_first_number)
# print(the_rest_of_the_numbers)
# 1
# [2, 3, 4, 5, 6]

# this also works to unpack a tuple, but puts it into a list
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
the_first_number, *the_rest_of_the_numbers = my_tuple
# print(the_first_number)
# print(the_rest_of_the_numbers)
# 1
# [2, 3, 4, 5, 6, 7, 8, 9]


# you can use an asterisk to merge iterables into a new list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_second_list = [7, 8, 9]
my_new_list = [*my_tuple, *my_list, *my_second_list]
# print(my_new_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# when using a set you cannot expect the set's order to be maintained
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
my_new_list = [*my_tuple, *my_list, *my_set]
# print(my_new_list)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]


# you can also merge two or more dictionaries together using the double asterisk
first_dict = {"a": 1, "b": 2, "c": 3}
second_dict = {"d": 4, "e": 5, "f": 6}
third_dict = {"g": 7, "h": 8, "i": 9}
new_dict = {**first_dict, **second_dict, **third_dict}
# print(new_dict)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
