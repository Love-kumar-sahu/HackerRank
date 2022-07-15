#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
def check(G,P,k,o,n,b):
    for i in range(k):
        for j in range(o):
            if G[i+n][j+b] != P[i][j]:
                return False
    return True

def gridSearch(G, P):
    # Write your code here
    n = len(G)
    m = len(G[0])
    k = len(P)
    o = len(P[0])
    for i in range(n-k+1):
        for j in range(m-o+1):
            if G[i][j] == P[0][0]:
                if check(G,P,k,o,i,j):
                    return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
