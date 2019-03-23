import numpy as np

np.set_printoptions(sign=' ')
ls = list(map(float, input().strip().split()))
print(np.floor(np.array(ls)))
print(np.ceil(np.array(ls)))
print(np.rint(np.array(ls)))
