#strings, ordered, immutable, text representation

# multiline and documentation strings use triple quotes
# new line is included when printing
my_string = """Hello
world"""
print(my_string)
# new line is not included when printing
my_string = """Hello \
world"""
print(my_string)
#can access parts of string using indexes and ranges
print(my_string[1])
print(my_string[8:11])

#reverse a string using the slicing operator
reversedstring = "Reverse This String"[::-1]
print(reversedstring)

#iterate through the letters
for letter in "This is a string":
    print(letter)

if "is a" in "This is a string":
    print("yes")

print("is a" in "This is a string")

# strip method
mystring = "  string with spaces   "
print("*" + mystring + "*")
mystring = mystring.strip()
print("*" + mystring + "*")

#strip specific characters
mystring = mystring.strip("s")
print(mystring)

# upper and lower cases
print("Everything in Upper case".upper())
print("Everything in Lower case".lower())

# starts with, ends with
print("Everything in Upper case".startswith("Ev"))
print("Everything in Lower case".endswith("ase"))

# get the index
print("What is the index?".find("nde"))
print("What is the index?".find("ggg"))

# count the number of occurrences
print("What is the index?".count("e"))

# replace characters
print("What is the index?".replace("e", "h"))

# split string into list
my_list = "This is a string to split".split()
print(my_list)
my_list = "Split this string at the i character".split("i")
print(my_list)

# join a string array into a string using a blank string as the connecting character
new_string = ''.join(my_list)
print(new_string)
new_string = '*'.join(my_list)
print(new_string)

# f strings
var1 = "Bobby"
var2 = 63
print(f"{var1} is {var2} years old")
