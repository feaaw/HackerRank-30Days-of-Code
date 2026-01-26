# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    if is_Prime(n):
        print("Prime")
    else:
        print("Not prime")
