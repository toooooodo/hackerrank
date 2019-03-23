#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if 'PM' in s:
        # print(int(s[:2])+12)
        if s[:2] != '12':
            return str(int(s[:2]) + 12) + s[2:-2]
        else:
            return s[:-2]
    else:
        # return s[:-2]
        # return str(int(s[:2]) % 12) + s[2:-2]
        if s[:2] != '12':
            return s[:-2]
        else:
            return '00' + s[2:-2]



if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    # f.write(result + '\n')
    #
    # f.close()
