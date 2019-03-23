import numpy

array = numpy.array(input().split(), dtype=float)
print(numpy.polyval(array, int(input())))
