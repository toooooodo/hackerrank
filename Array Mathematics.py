import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    a, b = (np.array([input().strip().split() for _ in range(n)], dtype=int) for _ in range(2))
    print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')
    # n, m = map(int, input().strip().split())
    # m1, m2 = [], []
    # for _ in range(n):
    #     ls = list(map(int, input().strip().split()))
    #     m1.append(ls)
    # for _ in range(n):
    #     ls = list(map(int, input().strip().split()))
    #     m2.append(ls)
    # a = np.array(m1, dtype=int)
    # b = np.array(m2, dtype=int)
    # print(np.add(a, b))
    # print(np.subtract(a, b))
    # print(np.multiply(a, b))
    # print(a//b)
    # print(np.mod(a, b))
    # print(np.power(a, b))
