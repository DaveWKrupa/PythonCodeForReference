

def print_values(a, b, c):
    print(a, b, c)


# the following are all equivalent
# print_values(1, 2, 3)
# print_values(a=1, b=2, c=3)
# print_values(c=3, a=1, b=2)
# print_values(1, c=3, b=2)
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3


# default values have to come at the end of the parameters list
# def foo(a, b, c, d=4)  # this is valid
# def foo(a, b=4, c, d)  # this will throw a SyntaxError


# you can pass args and kwargs at the end of the parameters list
# for *args it is the single asterisk that says you can pass multiple parameter values
# and for **kwargs it is the double asterisks that says you can pass multiple key value pairs
# *args is a tuple
# **kwargs is a dictionary
# so the following two are equivalent
# def foo(a, b, *args, **kwargs)
# def foo(a, b, *c, **d)
# but args and kwargs are usually used as a standard


def many_parameters(a, b, *args, **kwargs):
    print(a, b)
    # loop through *args tuple
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])


# many_parameters(1, 2, 3, 4, 5, six=6, seven=7, eight=8)
# 1 2
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


# this does not work, it will throw an error
# asterisk_func_one(1, 2, 3, 4)  #TypeError: asterisk_func_one() takes 2 positional arguments but 4 were given
# asterisk_func_one(1, 2, 3, 4, 5)  #TypeError: asterisk_func_one() takes 2 positional arguments but 5 were given

# this works because the last two arguments are named
# asterisk_func_one(1, 2, c=3, d=4)
# 1 2 3 4


def asterisk_func_two(*, a, b, c, d):
    print(a, b, c, d)


# asterisk_func_two(1, 2, c=3, d=4)  # TypeError: asterisk_func_two()
# # takes 0 positional arguments but 2 positional arguments (and 2 keyword-only arguments) were given

# asterisk_func_two(a=1, b=2, c=3, d=4)
# 1 2 3 4


# when *args is in a parameter position and there are parameters after that
# then all the parameters to the right of *args must be passed in by name
def args_first_func(a, b, *args, first_name, last_name):
    print(a, b)
    for arg in args:
        print(arg)
    print(first_name, last_name)


# args_first_func(1, 2, 3, 4, 5, first_name="Dave", last_name="Krupa")
# 1 2
# 3
# 4
# 5
# Dave Krupa


# unpacking arguments is a way to pass an iterable to a function instead of individual values
def foo(a, b, c):
    print(a, b, c)


my_list = [9, 8, 7]
# use an asterisk next to the list name to unpack it into the argument list
# foo(*my_list)
# 9 8 7

# this will throw an error
# my_list = [9, 8, 7, 6]
# foo(*my_list)  # TypeError: foo() takes 3 positional arguments but 4 were given

# a tuple also works
my_tuple = (5, 6, 7)
# foo(*my_tuple)
# 5 6 7

my_set = {3, 4, 5}
# foo(*my_set)
# 3 4 5

# this actually passes in the keys, not the values if you only use one asterisk
# but if you use two asterisks it works provided the key names match the parameter names
# and there are the same number of arguments as parameters
my_dict = {"a": 4, "b": 5, "c": 6}
# foo(*my_dict)
# a b c
# foo(**my_dict)
# 4 5 6


# immutable datatypes passed in as arguments are passed in by value
def print_this_argument(x):
    x = x + 10
    print(x)


immutable_value = 6
# print_this_argument(immutable_value)
# print(immutable_value)
# 16
# 6


def print_this_argument_two(x):
    x.append(12)
    print(x)


# mutable datatypes passed in are by reference so changes are saved to original
mutable_list = [1, 2, 3, 4]
# print_this_argument_two(mutable_list)
# print(mutable_list)
# [1, 2, 3, 4, 12]
# [1, 2, 3, 4, 12]


# reassigning a list in the function will cause the list to become a local variable
def print_this_argument_three(x):
    x = [8, 9, 10]
    print(x)


# print_this_argument_three(mutable_list)
# print(mutable_list)
# [8, 9, 10]
# [1, 2, 3, 4]


# the next two functions append items to the passed in list
# but a += operator changes the original list
# and the x = x + [8, 9, 10] changes x into a local copy
def print_this_argument_four(x):
    x += [8, 9, 10]
    print(x)


def print_this_argument_five(x):
    x = x + [8, 9, 10]
    print(x)


# list_one = [1, 2, 3]
# print_this_argument_three(list_one)
# print(list_one)
# [8, 9, 10]
# [1, 2, 3]
#
# list_one = [1, 2, 3]
# print_this_argument_four(list_one)
# print(list_one)
# [1, 2, 3, 8, 9, 10]
# [1, 2, 3, 8, 9, 10]
