#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    frn = 0
    sid = 0
    ze = 0
    l = len(A)
    c = len(A[0])
    for i in range(l):
        pre = 0
        for j in range(c):
            if A[i][j] == 0:
                ze+=1
            frn += abs(pre - A[i][j])
            pre = A[i][j]
        frn += A[i][j]
    for i in range(c):
        pre  = 0 
        for j in range(l):
            sid += abs(pre - A[j][i])
            pre = A[j][i]
        sid += A[j][i]
    return frn+sid+(c*l-ze)*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
