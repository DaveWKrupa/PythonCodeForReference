

two_dim_array = [[1, 2, 3], [4, 5, 5], [7, 8, 9], [10]]
print(two_dim_array)

try:
    for index1 in range(4):
        for index2 in range(3):
            print(two_dim_array[index1][index2])

except IndexError as berr:
    print(berr)
except ZeroDivisionError as err:
    print(err)
except ValueError as verr:
    print(verr)
print("Done")

# [[1, 2, 3], [4, 5, 5], [7, 8, 9], [10]]
# 1
# 2
# 3
# 4
# 5
# 5
# 7
# 8
# 9
# 10
# list index out of range
# Done