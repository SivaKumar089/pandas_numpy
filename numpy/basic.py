import numpy as np

# arr = np.array((1, 2, 3, 4, 5))

# arr = np.array(42)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print('number of dimensions :', arr.ndim)

# arr=np.array([1,2,3,4])
# print(arr[1])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[::3])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:5])
# print(arr[0:3, 2])


# arr = np.array([1, 2, 3, 4])

# arr = np.array(['apple', 'banana', 'cherry'])
# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr.dtype)



arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)
# newarr = arr.reshape(2, 3, 2)

# print(newarr)



# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   print(x)


# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 8)

# print(x)


# arr = np.array([3, 2, 0, 1])
# arr = np.array([True, False, True])
# arr = np.array(['banana', 'cherry', 'apple'])
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# # print(arr)

# print(np.sort(arr))

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)