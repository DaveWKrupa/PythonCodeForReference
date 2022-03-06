

def adder(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# print(adder(1, 2))
# print(adder(1, 2, 3))
# print(adder(1, 2, 5, 7, 8, 9, 10))
# 3
# 6
# 42


def myprint(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} is {v} years old')


myprint(Bob=20, Mike=40, Sam=17)
# Bob is 20 years old
# Mike is 40 years old
# Sam is 17 years old
