#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def en(s,d,sr):
    r=""
    t=0
    n=len(sr)
    arr1 = [["" for i in range(s+1)] for j in range(d+1)]
    for i in range(s):
        for j in range(d):
            if(t<n):
                arr1[i][j] = sr[t]
                t=t+1
    t=0
    for i in range(d):
        for j in range(s):
            r = r+arr1[j][i]
        r = r + " "
    return r
    

def encryption(s):
    # Write your code here
    n = len(s)
    sm = int(n**0.5)
    b = sm+1
    if(sm == n**0.5):
        return en(sm,sm,s)
    elif(sm*b>=n):
        return en(sm,b,s)
    else:
        return en(sm+1,b,s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
