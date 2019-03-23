# import numpy as np
#
# if __name__ == '__main__':
#     ls = list(map(int, input().rstrip().split()))
#     ls.reverse()
#     a = np.array(ls, float)
#     print(a)


import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
