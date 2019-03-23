import numpy

numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())

matrix = numpy.array([input().split() for _ in range(n)], dtype=int)
print(numpy.mean(matrix, axis=1), numpy.var(matrix, axis=0), numpy.std(matrix, axis=None), sep='\n')
# print(numpy.mean(matrix, axis=1))
# print(numpy.var(matrix, axis=0))
# print(numpy.std(matrix, axis=None))
