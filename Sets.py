#sets: unordered, mutable, no duplicates

mysetnumbers = {7, 21, 1, 3, 8, 5, 9, 0, 6, 4}
# print(mysetnumbers)
# {0, 1, 3, 4, 5, 6, 7, 8, 9, 21} #it put it in numerical order

mysetletters = {"w", "f", "y", "e", "c"}
# print(mysetletters)
# {'c', 'f', 'y', 'e', 'w'}

mysetwithdupes = {1, 2, 3, 1, 2, 3}  # only 1 of each will be saved with the set, no error though
# print(mysetwithdupes)
# {1, 2, 3}


#
# #use the set function to create a set from a list
mylist = [9, 8, 7]
mysetfromlist = set(mylist)
# print(mysetfromlist)
# {8, 9, 7}


# #pass a string to a set function to find out how many unique letters are in it
letters = "supercalafragilisticexpialidotious"
lettersset = set(letters)
# print(lettersset)
# print(len(lettersset))
# {'f', 'p', 'g', 'i', 'x', 'a', 't', 'u', 'c', 'd', 'o', 'r', 'e', 's', 'l'}
# 15

#
# # create an empty set
# # wrong way
not_a_set = {}
# print(type(not_a_set))
# <class 'dict'>

# # now the right way
is_a_set = set()
# print(type(is_a_set))
# <class 'set'>

#
# # use add method
is_a_set.add("one")
is_a_set.add("two")
is_a_set.add("three")
is_a_set.add("four")
is_a_set.add("five")
is_a_set.add("six")
# print(is_a_set)
# {'four', 'two', 'five', 'three', 'one', 'six'}

#
# #iterating over a set
# for item in is_a_set:
#     print(item)
# three
# five
# two
# one
# six
# four


#
# # use remove method
# print(is_a_set)
# {'two', 'five', 'three', 'six', 'four', 'one'}
is_a_set.remove("three")  # this will throw a key error if the element doesn't exist
# is_a_set.remove("three")  #  KeyError: 'three'
# print(is_a_set)
# {'two', 'five', 'six', 'four', 'one'}

# use the discard method
is_a_set.discard("six")
is_a_set.discard("six")  # this will not throw an error if the element doesn't exist
# print(is_a_set)
# {'two', 'five', 'four', 'one'}

# # check for item
# if "four" in is_a_set:
#     print("Four is in set")
# Four is in set

# # pop method removes an arbitrary value from the list
# print(is_a_set.pop())  # returns the value and removes it
# five
# print(is_a_set)
# {'four', 'two', 'one'}


#
# # clear the set
# is_a_set.clear()
# print(is_a_set)

#
# # union method to join two sets
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

oddsandevens = odds.union(evens)
# print(oddsandevens)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

#
# # intersection takes items that are in both sets
intersectionvalues = odds.intersection(primes)
# print(intersectionvalues)
# {3, 5, 7}

#
# # difference will take all the items in the first set that are not in the second set
diff = odds.difference(primes)
# print(diff)
# {1, 9}

#
sdiff = odds.symmetric_difference(primes)
# print(sdiff)
# {1, 2, 9}

#
# # combine two sets using the update method
seta = {1, 2, 3, 4}
setb = {3, 4, 5, 6, 7}
seta.update(setb)
# print(seta)
# {1, 2, 3, 4, 5, 6, 7}

#
# # intersection update keeps only numbers in both sets
setc = {1, 2, 3, 4}
setd = {3, 4, 5, 6, 7}
setc.intersection_update(setd)
# print(setc)
# {3, 4}

#
# # difference update
sete = {1, 2, 3, 4}
setf = {3, 4, 5, 6, 7}
sete.difference_update(setf)
# print(sete)
# {1, 2}

#
# # symmetric difference
setg = {1, 2, 3, 4, 5, 6, 7, 8, 9}
seth = {1, 2, 3, 10, 11, 12}
setg.symmetric_difference_update(seth)
# print(setg)
# {4, 5, 6, 7, 8, 9, 10, 11, 12}

#
# # subsets
seti = {1, 2, 3}
setj = {1, 2, 3, 4, 5, 6}
# print(seti.issubset(setj))  # seti is a subset of setj
# True

#
# # superset if first set contains all the numbers in the second set
# print(setj.issuperset(seti))  # setj is a superset of seti
# True


#
# # disjoint is true if the two sets do not contain any of the same elements
# print(seti.isdisjoint(setj))  # returns false
# False

# setk = {1, 2, 3}
# setl = {4, 5, 6}
# print(setk.isdisjoint(setl))  #returns true
# True
#

myfrozenset = frozenset([1, 2, 3])
# print(myfrozenset)
# frozenset({1, 2, 3})
# print(set(myfrozenset))
# {1, 2, 3}

# # will error if you try to change it
# #myfrozenset.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
#
#

