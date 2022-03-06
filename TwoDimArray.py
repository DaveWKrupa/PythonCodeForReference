two_dim_array = [[1, 2, 3], [4, 5, 5], [7, 8, 9], [10, 11, 12]]
print(two_dim_array)

for index1 in range(4):
    for index2 in range(3):
        print(two_dim_array[index1][index2])

for row in two_dim_array:
    for col in row:
        print(col)

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