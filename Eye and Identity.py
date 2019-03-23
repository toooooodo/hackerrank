import numpy

if __name__ == '__main__':
    # numpy.set_printoptions(legacy='1.13')
    # n, m = input().strip().split()
    # n, m = int(n), int(m)
    # print(numpy.eye(n, m, k=0))
    print(str(numpy.eye(*map(int, input().split()))).replace('1', ' 1').replace('0', ' 0'))
