import numpy

n, m = map(int, input().strip().split())

matrix = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
print(numpy.prod(numpy.sum(matrix, axis=0)))
