import numpy as np
from math import ceil
if __name__ == '__main__':
    region = np.array(
        [[73, 67, 43],
        [71, 134, 89],
        [56, 32, 98],
        [85, 46, 12],
        [58, 36, 26]]
                   )
    weights = np.array([0.3, 0.2, 0.5])
    mul = np.matmul(region, weights)
    print(region.shape)
    print(mul.shape)
    print(np.round(mul.sum()))
    print(ceil(mul.sum()))