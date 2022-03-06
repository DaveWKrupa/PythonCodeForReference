import copy

# with immutable values my_copy acts as expected
original = 7
my_copy = original  # this is a my_copy by reference
my_copy = 6  # this assigns the variable my_copy to a new address reference, separate from original
# print(original)
# print(my_copy)
# 7
# 6


# with mutable values my_copy acts as expected when setting the my_copy variable to a new list
original = [6, 7, 8]
my_copy = original  # this is a my_copy by reference
my_copy = [3, 4, 5]  # this assigns the variable my_copy to a new address reference, separate from original
# print(original)
# print(my_copy)
# [6, 7, 8]
# [3, 4, 5]


original = [6, 7, 8]
my_copy = original  # this is a my_copy by reference
my_copy[0] = 3  # this changes a value in the original reference, no new reference assigned
# print(original)
# print(my_copy)
# [3, 7, 8]
# [3, 7, 8]



# shallow my_copy; one level deep, only references of nested child objects
# deep my_copy: full independent my_copy

# the my_copy method makes a shallow my_copy by value
original = [6, 7, 8]
# all of the following make shallow copies
# my_copy = original.copy()
# my_copy = list(original)
my_copy = original[:]
# my_copy = copy.copy(original)  # this is a my_copy by value
my_copy[0] = 3  # this changes a value in the original reference, no new reference assigned
# print(original)
# print(my_copy)
# [6, 7, 8]
# [3, 7, 8]

# when we have a nested list it requires a deep copy
# a shallow copy will only keep the reference to the child lists
original = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
my_copy = copy.copy(original)
my_copy[0][1] = -11
# print(original)
# print(my_copy)
# [[1, -11, 3, 4, 5], [6, 7, 8, 9]]
# [[1, -11, 3, 4, 5], [6, 7, 8, 9]]

# as opposed to a deepcopy
original = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
my_copy = copy.deepcopy(original)
my_copy[0][1] = -11
# print(original)
# print(my_copy)
# [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
# [[1, -11, 3, 4, 5], [6, 7, 8, 9]]

# here is a shallow copy where the first level is copied by value but the second level is copied by reference
original = [1, 2, [1, 2, 3, 4, 5], [6, 7, 8, 9]]
my_copy = copy.copy(original)
my_copy[0] = 99
my_copy[2][1] = -11
# print(original)
# print(my_copy)
# [1, 2, [1, -11, 3, 4, 5], [6, 7, 8, 9]]
# [99, 2, [1, -11, 3, 4, 5], [6, 7, 8, 9]]

# but a deepcopy does all layers
original = [1, 2, [1, 2, 3, 4, 5], [6, 7, 8, 9]]
my_copy = copy.deepcopy(original)
my_copy[0] = 99
my_copy[2][1] = -11
# print(original)
# print(my_copy)
# [1, 2, [1, 2, 3, 4, 5], [6, 7, 8, 9]]
# [99, 2, [1, -11, 3, 4, 5], [6, 7, 8, 9]]