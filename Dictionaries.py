# dictionaries are unordered, mutable, key-value pairs
mydictionary = {
    "jan": "January", "feb": "February", "mar": "March",
}

# print(mydictionary["mar"])
# print(mydictionary.get("jan"))
# print(mydictionary.get("nov", "No such thing"))
# March
# January
# No such thing

# # dictionary function
mydictionary2 = dict(jan="January", feb="February", mar="March", jun="June")
#
# print(mydictionary2["mar"])
# print(mydictionary2.get("jan"))
# print(mydictionary2.get("nov", "No such thing"))
# March
# January
# No such thing

# new key value pairs added as needed
mydictionary2["jul"] = "July"
# print(mydictionary2["jul"])
# July



# # delete the jan key value pair from the dictionary
#print(mydictionary2)
del mydictionary2["jan"]
# print(mydictionary2)
# {'jan': 'January', 'feb': 'February', 'mar': 'March', 'jun': 'June', 'jul': 'July'}
# {'feb': 'February', 'mar': 'March', 'jun': 'June', 'jul': 'July'}

# # to remove the last key value pair use popitem
mydictionary2.popitem()
# print(mydictionary2)
# {'feb': 'February', 'mar': 'March', 'jun': 'June'}

#
# # check for key
# if "mar" in mydictionary2:
#     print(mydictionary2["mar"])
#

# # loop through the keys in the dictionary
# for thekey in mydictionary2:
#     print(thekey)
#

# # turn the keys into a list of the keys
mydictionary2 = dict(jan="January", feb="February", mar="March", jun="June")

dictkeys = mydictionary2.keys()
# print(dictkeys)
# for thekey in dictkeys:
#     print(thekey)

# dict_keys(['jan', 'feb', 'mar', 'jun'])
# jan
# feb
# mar
# jun

listkeys = list(mydictionary2.keys())
# print(listkeys)
# ['jan', 'feb', 'mar', 'jun']
#

# # loop through the values
# for value in mydictionary2.values():
#     print(value)
#

# # loop through the key, value pairs together
# for key, value in mydictionary2.items():
#     print(key, value)
#
# dictcopymem = mydictionary2  # copy by reference
# dictcopy1 = mydictionary2.copy()  # copy by value
# dictcopy2 = dict(mydictionary2)  # copy by value
#
# # overwrite a dictionary with new values if available
dictionary1 = {"name": "Joe", "address": "123 Fake St"}
dictionary2 = {"name": "Fred", "email": "fred@gmail.com"}
dictionary1.update(dictionary2)
# print(dictionary1)
# {'name': 'Fred', 'address': '123 Fake St', 'email': 'fred@gmail.com'}


#keys for dictionaries can be any immutable type, such as a tuple (but a list is mutable so can't be a key)
mytuple = (8, 7)
mydict = {mytuple: 45}
# print(mydict)
# {(8, 7): 45}
