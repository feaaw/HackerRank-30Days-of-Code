#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    binary_number =[]
    
    while n > 0:
        remainder = n % 2
        n = n // 2
        binary_number.append(remainder)
    
    current = 0
    maximum = 0
    
    for i in range(0, len(binary_number)):
        if binary_number[i] == 0:
            current = 0
        else:
            current += 1
            maximum = max(maximum, current)
    print(maximum)
