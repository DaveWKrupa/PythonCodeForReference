# lambda
from functools import reduce
# lambda arguments: expression

# set a variable equal to a lambda expression
# note that in PyCharm writing it this way gives the warning
# do not assign a lambda expression, use a def (error has be suppressed)
add10 = lambda x: x + 10

# now you can use the variable name like a function
# print(add10(5))
# 15

# which is the same as
def add10_func(x):
    return x + 10


# print(add10_func(5))
# 15
mult = lambda x, y: x * y

# print(mult(4, 5))
# 20

# use a lambda to sort a list

points2d = [(8, 2), (3, 11), (10, -5), (-1, 12), (4, 7), (2, 3), (11, -3)]
# print(points2d)
# [(8, 2), (3, 11), (10, -5), (-1, 12), (4, 7), (2, 3), (11, -3)]

# use the built in sorted function to sort based on index 0 (default)
points2d_sorted = sorted(points2d)
# print(points2d_sorted)
# [(-1, 12), (2, 3), (3, 11), (4, 7), (8, 2), (10, -5), (11, -3)]

# now use a lambda expression to set the sorted function using index 1
# the second argument in the sorted function has to be a lambda expression or a function
points2d_sorted = sorted(points2d, key=lambda x: x[1])
# print(points2d_sorted)
# [(10, -5), (11, -3), (8, 2), (2, 3), (4, 7), (3, 11), (-1, 12)]


# this is equivalent to creating a function that returns the value in each tuple in index 1
# here as in the lambda expression, the x argument value is the tuple, and returned is the value in index 1 of the tuple
def sort_by_y(x):
    return x[1]


# to use a function like this use the function name with no parameter
points2d_sorted = sorted(points2d, key=sort_by_y)
# print(points2d_sorted)
# [(10, -5), (11, -3), (8, 2), (2, 3), (4, 7), (3, 11), (-1, 12)]

# now sort the list based on the addition of the two values in the tuple
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
# print(points2d_sorted)
# [(10, -5), (2, 3), (11, -3), (8, 2), (-1, 12), (4, 7), (3, 11)]


# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
# print(list(b))
# [2, 4, 6, 8, 10]
# which is the same as the list comprehension syntax
c = [x * 2 for x in a]  # this is preferable to the map function
# print(c)
# [2, 4, 6, 8, 10]

# filter function, must return true or false, returns everything that returns true
# get only the even numbers in list a
b = filter(lambda x: x % 2 == 0, a)
# print(list(b))
# [2, 4]
# same as the list syntax
c = [x for x in a if x % 2 == 0]
# print(c)
# [2, 4]

# reduce function, returns a single value
# compute the product of all the elements
product_a = reduce(lambda x, y: x * y, a)
# print(product_a)
# 120




