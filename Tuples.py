import sys
import timeit

#tuples are ordered, immutable, can include duplicates
mytuple = ("Max", 28, "Boston")
# print(mytuple)
# ('Max', 28, 'Boston')
# print(type(mytuple))
# <class 'tuple'>


#
mytuple2 = "Roger", 8, "Psf"
# print(mytuple2)
# print(type(mytuple2))
# ('Roger', 8, 'Psf')
# <class 'tuple'>

# add a comma onto the end to turn a string into a tuple
mytuplenotatuple = "Roger"
# print(mytuplenotatuple)
# print(type(mytuplenotatuple))
# Roger
# <class 'str'>


mytupleisatupe = "Roger",
# print(mytupleisatupe)
# print(type(mytupleisatupe))
# ('Roger',)
# <class 'tuple'>

mylist = [1, 2, 3, 4]
# print(mylist)
# print(type(mylist))
# [1, 2, 3, 4]
# <class 'list'>

tuplecreatedfromlist = tuple([1, 2, 3, 4, 3, 6, 8])
# print(tuplecreatedfromlist)
# print(type(tuplecreatedfromlist))
# (1, 2, 3, 4, 3, 6, 8)
# <class 'tuple'>

listcreatedfromtuple = list(tuplecreatedfromlist)
# print(listcreatedfromtuple)
# print(type(listcreatedfromtuple))
# [1, 2, 3, 4, 3, 6, 8]
# <class 'list'>



#
# for i in tuplecreatedfromlist:
#     print(i)
#
# if "Roger" in mytuple2:
#     print("True")
# else:
#     print("False")
#
# if "Bobby" in mytuple2:
#     print("True")
# else:
#     print("False")
#
# print(tuplecreatedfromlist)
# print(len(tuplecreatedfromlist))
# print(tuplecreatedfromlist.count(3))  #count the number of 3s
# print(tuplecreatedfromlist.count(5))
# print(tuplecreatedfromlist.index(3))
# (1, 2, 3, 4, 3, 6, 8)
# 7
# 2
# 0
# 2


#
# #unpacking
name, age, city = mytuple
# print(name)
# print(age)
# print(city)
# Max
# 28
# Boston

#
i1, *i2, i3 = tuplecreatedfromlist
# print(i1)
# print(i2)
# print(i3)
# 1
# [2, 3, 4, 3, 6]
# 8

#
tuplesized = (1, 2, 3, 4, 5, 6, 7, 8, 9, "hello", True)
listsized = list(tuplesized)


# print(sys.getsizeof(tuplesized), "bytes")
# print(sys.getsizeof(listsized), "bytes")
# 128 bytes
# 144 bytes
#
# # time how long it takes to create 1 million tuples vs lists
# print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))
# print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))
# 0.005796200013719499
# 0.03486210003029555


