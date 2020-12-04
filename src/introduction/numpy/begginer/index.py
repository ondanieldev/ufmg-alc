"""
--------------------------------------------------------------------------------
All exercices are preceded by a comment that starts with a verb.
You can search for a specify verb to found the desired function easily.
The verbs are:
  - show;
  - create;
  - extract;
  - replace;
  - reshape;
  - concact;
  - get;
  - swap;
  - reverse;
--------------------------------------------------------------------------------
"""

import numpy as np

# show numpy version
print('#1', np.__version__)

# create array from 0 to 10
print('#2', np.arange(10))

# create boolean array
print('#3', np.full((3, 3), True, dtype=bool))

# extract odds from array
arr = np.arange(10)
print('#4', arr[arr % 2 == 1])

# replace odds to -1
arr = np.arange(10)
arr[arr % 2 == 1] = -1
print('#5', arr)

# replace without modify original
arr = np.arange(10)
copy = np.where(arr % 2 == -1, -1, arr)
print('#6', copy, arr)

# reshape array
arr = np.arange(10)
# -1 automatically decides the number of cols
print('#7', np.reshape(arr, (2, -1)))

# concat a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print('#8', np.concatenate((a, b)))

# concat a and b horizontally
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print('#9', np.concatenate((a, b), axis=1))

# create custom arrays without hardcode
a = np.array([1, 2, 3])
print('#10', np.concatenate((np.repeat(a, 3), np.tile(a, 3))))

# get the common items between arrays
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print('#11', np.intersect1d(a, b))

# remove from one array those items that exist in another
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
print('#12', np.setdiff1d(a, b))

# get the positions where elements of two arrays match
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print('#13', np.where(a == b))

# extract all numbers between a given range from a numpy array
a = np.array([2, 6, 1, 9, 10, 3, 27])
print('#14', a[(a >= 5) & (a <= 10)])


# get the intersect through a function VERY USEFULL [!]
def maxx(x, y):
    if x >= y:
        return x
    return y


pair_maxx = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print('#15', pair_maxx(a, b))

# swap two columns in a 2d numpy array
arr = np.arange(9).reshape(3, 3)
print('#16', arr, '\n', arr[:, [1, 0, 2]])

# swap two rows in a 2d numpy array
arr = np.arange(9).reshape(3, 3)
print('#17', arr, '\n', arr[[1, 0, 2], :])

# reverse the rows of a 2D array
arr = np.arange(9).reshape(3, 3)
print('#18', arr[::-1])

# reverse the columns of a 2D array
arr = np.arange(9).reshape(3, 3)
print('#19', arr[:, ::-1])

# create a 2D array containing random floats between 5 and 10
arr = np.random.uniform(5, 10, (5, 3))
print('#20', arr)

# show only 3 decimal places in python numpy array
rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print('#21', rand_arr)

# show prettier
np.set_printoptions(suppress=False)
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
np.set_printoptions(suppress=True, precision=6)
print('#22', rand_arr)

# show with limit the number of items printed in output of numpy array
np.set_printoptions(suppress=False)
a = np.arange(15)
np.set_printoptions(threshold=6, edgeitems=3)
print('#23', a)

# show with limit the number of items printed in output of numpy array
np.set_printoptions(threshold=6)
a = np.arange(15)
np.set_printoptions(threshold=np.nan)
print('#24', a)
