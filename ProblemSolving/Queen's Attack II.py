#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    mov = {'w':n-r_q,
    'we':min(n-r_q,n-c_q),
    'wq':min(n-r_q,c_q-1),
    'd':n-c_q,
    'a':c_q-1,
    's':r_q-1,
    'se':min(r_q-1,n-c_q),
    'sq':min(c_q-1,r_q-1)}
    for i in obstacles:
        if i[0] == r_q:
            if i[1] > c_q:
                mov['d']=min(mov['d'],i[1]-c_q-1)
            else:
                mov['a']= min(mov['a'],c_q-i[1]-1)
        elif i[1] == c_q:
            if i[0] > r_q:
                mov['w']= min(mov['w'],i[0]-r_q-1)
            else:
                mov['s']= min(mov['s'],r_q-i[0]-1)
        elif i[0] - i[1] == r_q - c_q:
            if i[1] > c_q:
                mov['we'] = min(mov['we'],min(i[1]-c_q-1,i[0]-r_q-1))
            else:
                mov['sq'] = min(mov['sq'],min(c_q-i[1]-1,r_q-i[0]-1))
        elif i[0]+i[1] == r_q+c_q:
            if i[0] > r_q:
                mov['wq'] = min(mov['wq'],min(i[0]-r_q-1,c_q-i[1]-1))
            else:
                mov['se'] = min(mov['se'],min(r_q-i[0]-1,i[1]-c_q-1))
    return sum(mov.values())
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
