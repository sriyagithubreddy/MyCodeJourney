import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length=len(arr)
    r1=0
    r2=0
    for i in range(length):
        r1+=arr[i][length-i-1]
        r2+=arr[i][i]
    return abs(r1-r2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
