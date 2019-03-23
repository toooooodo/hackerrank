import numpy

if __name__ == '__main__':
    ls = list(map(int, input().rstrip().split()))
    print(numpy.zeros((ls), dtype=numpy.int))
    print(numpy.ones((ls), dtype=numpy.int))
    # for i in ls:
    #     print(numpy.zeros((i, i), dtype=numpy.int))
    # for i in ls:
    #     print(numpy.ones((i, i), dtype=numpy.int))
    # result1 = []
    # result2 = []
    # for i in ls:
    #     result1.append(numpy.zeros((i, i), dtype=numpy.int))
    # for i in ls:
    #     result2.append(numpy.ones((i, i), dtype=numpy.int))
    # print(result1)
    # print(result2)
