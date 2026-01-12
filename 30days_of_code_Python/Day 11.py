#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = float('-inf')

    for i in range(1, 5):
        for j in range(1, 5):
            hourglass = (
                sum(arr[i - 1][j - 1:j + 2]) +
                arr[i][j] +
                sum(arr[i + 1][j - 1:j + 2])
            )
            max_sum = max(max_sum, hourglass)
            
    print(max_sum)
