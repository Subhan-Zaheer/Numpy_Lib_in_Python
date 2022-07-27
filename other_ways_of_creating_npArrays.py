import numpy as np
if __name__ == '__main__':
    """
    Arange module in np works as range function we have used in for loop.
    but range function does not return a list. Arange function returns one.
    """
    a = np.arange(100)
    print(a)
    b = np.arange(10, 150, 10)
    print(b)
    """
    np.random.permutation function will shuffle the elements of np array.
    """
    c = np.random.permutation(b)
    print(c)
    print(b)
    c.sort()
    print(c)
    """
    Reshape function will convert the 1-D array into multi dimensional array.
    """
    d = a.reshape(4, 5, 5)
    print(d)
    print(d.ndim)
    
