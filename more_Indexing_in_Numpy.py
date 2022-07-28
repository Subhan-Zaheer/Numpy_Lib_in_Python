import numpy as np

if __name__ == '__main__':
    a = np.arange(11)
    b = a[[1, 4, 5]]
    print(b)
    b[0] = 6
    print(b)
    print(a)
    print(a[[True, True, False, False, True, True, True, False, False, True, True]])
    c = a[a < 8]
    print(c)
    ### & operator when both operands are iterable and 'and' operator is used when both operands are single values.
    ### | operator when both operands are iterable and 'or' operator is used when both operands are single values.
    ### ~ operator when both operands are iterable and 'not' operator is used when both operands are single values.
    c = a[(a < 8) & (a > 4)]
    print(c)