import numpy as np


def matmul(a, b):
    pass

if __name__ == '__main__':

    a = np.arange(6)
    a = a.reshape(2,3)

    b = np.arange(10,16)
    b = b.reshape(3,2)

    print(a)
    print(b)

    print(b[0,1])

    print(a.shape[1])
    c = np.matmul(a,b)
    print(c)

