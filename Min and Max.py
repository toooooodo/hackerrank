import numpy

n, m = map(int, input().strip().split())

matrix = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
print(numpy.max(numpy.min(matrix, axis=1)))
