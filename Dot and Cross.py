import numpy

n = int(input())
a, b = (numpy.array([input().strip().split() for _ in range(n)], dtype=int) for _ in range(2))
print(numpy.dot(a, b))
