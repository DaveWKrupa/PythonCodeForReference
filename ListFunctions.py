#Lists: ordered, mutable, allows duplicate elements

lucky_numbers = [3, 6, 7]
lucky_letters = ["a", "r", "z"]
lucky_letters_two = ["g", "b"]
# print(lucky_letters[1])
# print(lucky_letters[-1])  # negative numbers start with the last index and work backwards
# r
# z


# #append the second array onto the first
lucky_letters_two.extend(lucky_letters)
# print(lucky_letters_two)
# ['g', 'b', 'a', 'r', 'z']


lucky_letters_two.append("hi there")
# print(lucky_letters_two)
# ['g', 'b', 'a', 'r', 'z', 'hi there']
# print(lucky_letters_two.index("hi there"))
# 5

# take "hi there" out of the list
lucky_letters_two.remove("hi there")
# print(lucky_letters_two)
# ['g', 'b', 'a', 'r', 'z']

#print(lucky_letters_two.index("hi there"))  # ValueError: 'hi there' is not in list

lucky_letters_two.insert(3, "3rd position")
# print(lucky_letters_two)
# ['g', 'b', 'a', '3rd position', 'r', 'z']

lucky_letters_two.pop()
# print(lucky_letters_two)
# ['g', 'b', 'a', '3rd position', 'r']

lucky_letters_two.sort()
# print(lucky_letters_two)
# ['3rd position', 'a', 'b', 'g', 'r']

lucky_letters_two.reverse()
# print(lucky_letters_two)
# ['r', 'g', 'b', 'a', '3rd position']

luck_numbers_and_letters = lucky_numbers + lucky_letters
# print(luck_numbers_and_letters)
# [3, 6, 7, 'a', 'r', 'z']

# print(lucky_letters)
lucky_letter_copy = lucky_letters.copy()
# print(lucky_letter_copy)
lucky_numbers.clear()
# print(lucky_numbers)

#
#
listFunctionList = list()
listFunctionList.append("Hey There")
# print(listFunctionList)
# ['Hey There']

listFunctionList = listFunctionList + lucky_letters
# print(listFunctionList)
# ['Hey There', 'a', 'r', 'z']

# the = operator creates a copy of the reference, not value
lucky_letters_copy = lucky_letters
lucky_letters.append("new item")
# print(lucky_letters)
# ['a', 'r', 'z', 'new item']


# Three ways to copy by value
lucky_letters_copy_one = lucky_letters.copy()
lucky_letters_copy_two = list(lucky_letters)
lucky_letters_copy_three = lucky_letters[:]


mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
slice_a = mylist[2:5]
# print(slice_a)
# ['c', 'd', 'e']

slice_b = mylist[:6]
# print(slice_b)
# ['a', 'b', 'c', 'd', 'e', 'f']

slice_c = mylist[::3]
# print(slice_c)
# ['a', 'd', 'g', 'j', 'm']

slice_c = mylist[12:2:-2]
# print(slice_c)
# ['m', 'k', 'i', 'g', 'e']

listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listofnumberssquared = [i * i for i in listofnumbers]
# print(listofnumbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(listofnumberssquared)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

my_list = ['a'] * 6
# print(my_list)
# ['a', 'a', 'a', 'a', 'a', 'a']