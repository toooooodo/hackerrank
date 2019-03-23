#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # arr.sort()
    # min=sum(arr[])
    # print(sum[arr] - max(arr)sum[arr] - min(arr))
    print("%d %d" % (sum(arr) - max(arr), sum(arr) - min(arr)))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
