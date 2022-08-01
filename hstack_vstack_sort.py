import numpy as np
import timeit as tm

if __name__ == '__main__':
    a = np.round(10*np.random.rand(2, 4))
    print(a)
    b = np.round(10*np.random.rand(2, 4))
    print(b)
    c = np.hstack((a, b))   # Will concatenate two arrays horizontally.
    print(c)
    d = np.vstack((a, b))   # Will concatenate two arrays vertically.
    print(d)
    d.sort(axis=0)   # This will sort the 2 d array by rows.
    d.sort(axis=1)   # This will sort the 2 d array by columns.
    print(d)
    str1 = np.array(['d', 'a', 'c', 'b'])
    str1.sort()
    print(str1)
    print(str1[::-1])
