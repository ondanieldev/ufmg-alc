import numpy as np

# array to work with
np.random.seed(21)
random_integers = np.random.randint(1, high=500000, size=(20, 5))
print('#1', random_integers)

# average valeu of the second column
np.set_printoptions(precision=2)
print('#2', np.average(random_integers[:, 1]))

# average value of the first 5 rows of the third and fourth columns
print('#3', np.average(random_integers[0:4, 2:4]))

# expected result of first_matrix + second_matrix
# 1 2 3   +   1 2 3   =   2 4 6
# 4 5 6                   5 7 9
first_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print('#4', first_matrix)
second_matrix = np.array([1, 2, 3])
print('#4', second_matrix)

# expected result of my_vector[selection]
# [2, 4, 6]
my_vector = np.array([1, 2, 3, 4, 5, 6])
selection = my_vector % 2 == 0
print('#5', my_vector)
print('#5', selection)

# check two previous results
print('#6 for #4', first_matrix + second_matrix)
print('#6 for #5', my_vector[selection])

# view vs copy
# view -> arrays appoints to the same data, but displays it differently
# copy -> arrays does not appoint to the same data
# get a view -> slice array array[1:2]
# get a copy -> fancy index array array[1,2]
# changes in view just will be propagated if you use simple index a[i] = n
my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
my_slice[0] = -1
print('#7: both will be changed', my_array, my_slice)
my_array = np.array([1, 2, 3])
my_slice = my_array[[1, 2]]
my_slice[0] = -1
print('#7: just slice will be changed', my_array, my_slice)
my_array = np.array([[1, 2, 3], [4, 5, 6]])
my_slice = my_array[:, 1:3]
print('#8', my_array, my_slice)
my_array[:, :] = my_array * 2
print('#9', my_array, my_slice)
my_array = my_array * 2
print('#10', my_array, my_slice)
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print('#11', my_array)
my_slice = my_array[:, 1:3].copy()
print('#11', my_slice)
my_array[:, :] = my_array * 2
print('#11', my_array, my_slice)
