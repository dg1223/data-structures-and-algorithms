import numpy as np

a = np.matrix([[1,2,3,4], [5,6,7,8],[9,10,11,12]])

# trasponse
# transposed_matrix = zip(*a)
# unpack_transposed_matrix = [ row for row in transposed_matrix]
# print(np.array(unpack_transposed_matrix))

# raw transposed form
# x, y, z = zip(*zip(*a))

# copying a matrix
# copied_matrix = [row[:] for row in a]
copied_matrix = a.copy()
# print(len(copied_matrix))

zero_matrix = [[0 for _ in range(np.shape(a)[1])] for _ in range(np.shape(a)[0])]

zero_matrix_list = [[]]
for i in range(3):
    for j in range(4):
        zero_matrix_list.append(0)

print(a)
print(zero_matrix)
print(zero_matrix_list)
print(np.zeros((3, 4)))

