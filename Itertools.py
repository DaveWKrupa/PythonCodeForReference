# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
from itertools import count, cycle, repeat
import operator

# product takes lists and computes the cartesian product
# the output is an iterable list of tuples
a = [1, 2]
b = [3, 4]
prod = product(a, b)
# print(list(prod))
# [(1, 3), (1, 4), (2, 3), (2, 4)]

prod
a = [1, 2, 3]
b = [4, 5, 6]
prod = product(a, b)
# print(list(prod))
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
prod = product(a, b, c)
# print(list(prod))

# permutations returns all possible orderings of an input
a = [1, 2, 3]
perm = permutations(a)
# print(list(perm))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = permutations(a, 2)  # length of 2 means only two items
# print(list(perm))
a = [1, 2, 3, 3]
perm = permutations(a)
# print(list(perm))

# combinations, makes all possible combinations with specified length (length is mandatory)
a = [1, 2, 3, 4]
comb = combinations(a, 2)
# print(list(comb))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
comb = combinations(a, 3)
# print(list(comb))

# combinations_with_replacement is like combinations but also combines elements with themselves
a = [1, 2, 3, 4]
comb_w = combinations_with_replacement(a, 2)
# print(list(comb_w))
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


# accumulate takes a list of numbers and accumulates them
# that is, each item in the new list is the sum total of all items in the original list before it
a = [1, 2, 3, 4]
acc = accumulate(a)
# print(list(acc))
# [1, 3, 6, 10]

# func=operator.mul tells accumulate to multiply instead of add
acc = accumulate(a, func=operator.mul)
# print(list(acc))
# [1, 2, 6, 24]

# max will make a new list where the next item is the largest number encountered so far
a = [2, 7, 4, 9, 12, 11, 1]
acc = accumulate(a, func=max)
# print(list(acc))
# [2, 7, 7, 9, 12, 12, 12]
a = [8, 7, 10, 4, 9, 12, 11, 1]
acc = accumulate(a, func=min)


# print(list(acc))
# [8, 7, 7, 4, 4, 4, 4, 1]

# groupby uses a boolean function to determine groupings
def smaller_than_4(x):
    return x < 4


a = [1, 2, 9, 4, 3]
group_obj = groupby(a, key=smaller_than_4)
#  print(group_obj)
# <itertools.groupby object at 0x000001F2F042A6B0>
# for key, value in group_obj:
#     print(key)
#     print(list(value))
# True
# [1, 2]
# False
# [9, 4]
# True
# [3]

# the same using a Lambda expression
group_obj = groupby(a, key=lambda x: x < 4)
# for key, value in group_obj:
#     print(key)
#     print(list(value))


a = ["Tom", "Mike", "Jim", "Fred", "Jim"]
group_obj = groupby(a, key=lambda x: x == "Jim")
# for key, value in group_obj:
#     print(key)
#     print(list(value))
# False
# ['Tom', 'Mike']
# True
# ['Jim']
# False
# ['Fred']
# True
# ['Jim']

# this next one groups all dictionary objects using the age key
people = [{"name": "Jim", "age": 25}, {"name": "Bob", "age": 25},
          {'name': "Rick", "age": 26}, {"name": "Dick", "age": 26},
          {'name': "Mike", "age": 28}, {"name": "Joe", "age": 29}]

group_obj = groupby(people, key=lambda x: x["age"])
# for key, value in group_obj:
#     print(key)
#     print(list(value))
# 25
# [{'name': 'Jim', 'age': 25}, {'name': 'Bob', 'age': 25}]
# 26
# [{'name': 'Rick', 'age': 26}, {'name': 'Dick', 'age': 26}]
# 28
# [{'name': 'Mike', 'age': 28}]
# 29
# [{'name': 'Joe', 'age': 29}]

# infinite iterators operate until a break is triggered
# count starts at an integer and increases by 1
# for i in count(3):
#     print(i)
#     if i > 10:
#         break
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

# cycle loops through a list infinitely until a break is triggered
a = [1, 2, 3]
counter = 0
# for x in cycle(a):
#     print(x)
#     counter += 1
#     if counter > 12:
#         break
# 1
# 2
# 3
# 1
# 2
# 3
# 1
# 2
# 3
# 1
# 2
# 3
# 1

# repeats something for the indicated number of times
# for x in repeat("a", 6):
#     print(x)
# a
# a
# a
# a
# a
# a


