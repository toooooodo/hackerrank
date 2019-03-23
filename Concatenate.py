import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().rstrip().split())
    arr1 = []
    arr2 = []
    for i in range(n):
        arr1.append(list(map(int, input().rstrip().split())))
    for i in range(m):
        arr2.append(list(map(int, input().rstrip().split())))
    print(numpy.concatenate((numpy.array(arr1), numpy.array(arr2))))
