import numpy
numpy.set_printoptions(legacy='1.13')

n = int(input())
print(numpy.linalg.det([list(map(float, input().split())) for _ in range(n)]))
