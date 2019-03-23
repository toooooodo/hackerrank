import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    # array = numpy.array([input().strip().split() for _ in range(n)], int)
    # print(array.transpose())
    # print(array.flatten())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(numpy.array(arr).transpose())
    print(numpy.array(arr).flatten())
