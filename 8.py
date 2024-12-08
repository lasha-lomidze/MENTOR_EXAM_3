
# Write a function that finds the k-th smallest element in an unsorted array.

def func(arr, n):
    return sorted(arr)[n-1]   # ubralod davasortirot da amovighot n-th elementoi


# test cases 8:
print(func([3, 2, 1, 5, 6, 4], 2))
print(func([3, 2, 1, 5, 6, 4], 4))
print(func([7, 10, 4, 3, 20, 15], 3))
print(func([1, 2, 3, 4, 5], 1))
print(func([3, 2, 1, 5, 6, 4], 5))