import numpy as np

"""
print(np.array([1, 2, 3, 4, 5]))
print(np.array(['1', 2, 3, 4, 5]))
print(np.array([1, 2, 3, 4], dtype=float))
print(np.zeros(10))
print(np.ones((3, 2)))
print(np.full((3, 2), 3.14))
print(np.arange(10))
print(np.eye(3))

a3 = np.random.randint(10, size=(3, 4, 5))
print(a3.ndim)
print(a3.shape)
print(a3.size)  # != len
print(a3[0, 2], a3[0][2])
"""

"""
a = np.arange(10)
print(a, a[-5:])
print(a, a[:-5])

a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2, a2[:, 0], a2[0, :])

a2_sub = a2[2:, 2:]  # share pointers
a2_sub = a2[2:, 2:].copy()  # dont share pointers

print(np.arange(1, 10).reshape((3, 3)))
"""

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.concatenate([a1, a2])
print(a3)

a4 = np.array([[1, 2, 3], [4, 5, 6]])
a5 = np.concatenate([a4, a4])
print(a5)
a6 = np.concatenate([a4, a4], axis=1)
print(a6)
