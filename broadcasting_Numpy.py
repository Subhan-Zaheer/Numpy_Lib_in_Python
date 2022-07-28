import numpy as np

if __name__ == '__main__':
    """
    In this example we create a 2 dimensional matrix and then add 5 in each element of this matrix.
    for ex
    [1 2] + [5 5]
    [3 4]   [5 5]
    """
    a = np.round(10*np.random.rand(2, 2))
    print(a)
    a = a + 5
    print(a)
    """
    In this example we create a two dimensional array and add it to another 2 dimensional array.
    [1 2] + [1]
    [3 4]   [3]
    """
    b = np.round(10*np.random.rand(2, 1))
    print(b)
    a = a + b
    print(a)