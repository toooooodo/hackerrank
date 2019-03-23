#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # row = int(math.sqrt(len(arr)))
    # sum1 = sum([arr[i * row + i] for i in range(row)])
    # sum2 = sum([arr[i * row + row - 1 - i] for i in range(row)])
    # return abs(sum1 - sum2)
    sum1 = sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr) - i - 1]
    return abs(sum1 - sum2)


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
