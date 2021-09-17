#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    N, swaps = len(arr), 0
    minimum = min(arr) # O(N)


    for i in range(N): # O(N)
        ei = arr[i]-minimum
        while i != ei: # Will solve all cases for 5 1 2 3 4
            arr[i], arr[ei] = arr[ei], arr[i]
            ei = arr[i]-minimum
            swaps += 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

