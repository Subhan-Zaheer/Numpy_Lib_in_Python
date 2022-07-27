import numpy as np

if __name__ == '__main__':
    """
    Single Dimesion arrays
    """
    # a = np.array([1, 2, 3, 4, 5], dtype='i')
    # print(a)
    # print(a.dtype)
    # b = np.array(["a", "b", "c"], dtype='str')
    # print(b)
    # print(b.dtype)
    # print(b.size)
    # print(b.put(2, "d"))
    # print(b)
    """
    Multi Dimension Arrays
    """
    a = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    # In case of multi dimension arrays all the elements of sub array should remain same.
    # For example if a sub array has 3 elements in it.
    # like in above example all the following sub arrays should have same numbers of element.
    print(a)
    print(a[0, 1, 1])
    print(a.size)
    print(a.ndim)
    print(a.shape)
    print(a.nbytes)