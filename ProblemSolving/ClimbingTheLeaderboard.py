import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
from collections import Counter
from bisect import bisect_left

def climbingLeaderboard(ranked, player):
    # Write your code here
    counts = Counter(ranked)
    counts = sorted(counts)
    n = len(counts)
    re = []
    for a in player:
        i = bisect_left(counts, a)
        if i < n and counts[i]==a:
            print(n - i)
            re.append(n-i)
        else:
            re.append(n+1-i)
            print(n+1-i)
    return re

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()