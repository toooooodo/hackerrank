import numpy

lst = (list(map(int, input().rstrip().split())))
my_array = numpy.array(lst)
print(numpy.reshape(my_array, (3, 3)))
