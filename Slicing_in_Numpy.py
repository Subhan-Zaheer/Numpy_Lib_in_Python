
import numpy as np
import matplotlib as mpl

if __name__ == '__main__':
    a = np.arange(10)
    b = a[1:10:2]
    print(b)
    b[2] = 100
    print(b)
    print(a)
    print(a[::-1])
    print(a[::1])
    print(a[::2])
    print(a[::-2])
    # In above example b is not a copy of a . Basically b is pointing to same memory location of a .
    # If you want to make a copy of a to b then you should follow rules given below.
    c = a[::].copy()
    c[1] = 1200
    print(a)
    print(c)
    # That's how you can find index of specific number. Here we find the index of 100.
    arr_index = np.argwhere(a == 100)[0][0]
    print(arr_index)
    d = np.round(10*np.random.rand(5, 4))
    print(d)
    print(d[2, :])
    print(d[:, 2])
    print(d[1:4, 2:4])
    d.sort(axis= 0)
    d.sort(axis= 1)
    print(d)