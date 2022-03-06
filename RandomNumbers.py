import random  # pseudo random numbers
import secrets  # a more robust way to generate random number
import numpy as np
# pip install numpy

# use numpy to get random numbers
a = np.random.rand(3)  # get an array of 3 random numbers between 0 and 1
# print(a)
# [0.80390037 0.25504253 0.86910281]

# get a 2 dimensional array of random numbers
a = np.random.rand(3, 3)  # get an array of 3 random numbers between 0 and 1
# print(a)
# [[0.28295341 0.89197597 0.46127702]
#  [0.10737657 0.15359756 0.14849568]
#  [0.544936   0.19673547 0.99566798]]

# to get an integer from a range use randint
a = np.random.randint(3, 12)  # top number excluded
# print(a)
# 6

a = np.random.randint(3, 12, 3)  # return 3 numbers
# print(a)
# [7 8 7]

a = np.random.randint(3, 12, (3, 4))  # return 2 dimensional array with 3 rows and 4 columns
# print(a)
# [[ 8 11  9  6]
#  [ 8  9 11  9]
#  [ 5  4  3 10]]

# shuffle an array of arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(arr)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

np.random.shuffle(arr)
# print(arr)
# [[ 1  2  3]
#  [10 11 12]
#  [ 4  5  6]
#  [ 7  8  9]]


# random numbers using secrets
# this is supposed to be a true random number generator
# randbits passes back an integer from 0 to a value determined by the argument
# the argument specifies the number of bits to use to determine the top number
# for the example 4 it uses 4 bits
# that is to say from 0000 to 1111
# for each position it can be a 0 or 1 so a single bit has 2 possibilities
# 0 -> 2
# 00 -> 4
# 000 -> 8
# 0000 -> 16
# since 0 based the top possible number passed back would be 15
a = secrets.randbits(4)  # get a random value between 0 and 15
# print(a)

mylist = list("abcdefghijk")  # turn a string into a list of characters
a = secrets.choice(mylist)
# print(a)



#pseudo random numbers

a = random.random()
# decimal between 0 and 1
# print(a)
# 0.052669853085603346

b = random.uniform(3, 23)
# decimal between two provided values
# print(b)
# 4.319331271916571

c = random.randint(9, 52)  # random integer between 9 and 52 inclusive
# print(c)

# unlike randint, randrange will not include the top number (52 in this example)
d = random.randrange(9, 52, 3)  # start, stop, step
# print(d)

mylist = list("abcdefghijk")  # turn a string into a list of characters
# print(mylist)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# now get a random item from list
e = random.choice(mylist)
# print(e)

# now pick a unique selection of items
f = random.sample(mylist, 4)
# print(f)
# ['h', 'c', 'i', 'f']

# if you want to allow the same item to possibly be picked more than once can use choices
g = random.choices(mylist, k=7)
# print(g)
# ['g', 'a', 'f', 'j', 'd', 'b', 'f']

random.shuffle(mylist)
# print(mylist)
# ['f', 'e', 'k', 'c', 'g', 'j', 'a', 'd', 'b', 'h', 'i']

# setting the seed value will make the numbers predictable
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# 0.13436424411240122
# 2
# 0.13436424411240122
# 2
