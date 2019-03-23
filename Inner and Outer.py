import numpy

a, b = (numpy.array([input().split()], dtype=int) for _ in range(2))
# print(int(numpy.inner(a, b)))
print(int(numpy.inner(a, b)), numpy.outer(a, b), sep='\n')
