#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#
def ab(s,d):
    a =[]
    for i in d:
        a.append(i)
    for i in s:
        a.append(i)
    return a

def absolutePermutation(n, k):
    # Write your code here
    a = []
    c = []
    b = [-1]
    if k == 0:
        for i in range(1,n+1):
            a.append(i)
        return a
    if n % (2*k) == 0:
        for i in range(1,n+1,k*2):
            for j in range(i,i+k*2):
                c.append(j)
            print(i)
            print(c[i-1:k+i-1],0)
            print(c[(k+i)-1:(i+k*2)-1],1)
            for j in ab(c[i-1:(k+i)-1],c[(k+i)-1:(i+k*2)-1]):
                a.append(j)
        return a
    else:
        return b
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
