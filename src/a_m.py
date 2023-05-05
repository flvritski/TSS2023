import math
import os
def arrayManipulation(n, queries):
    arr = [0] * n

    if (n < 3) or (n>10000000):
        return -1    
    for query in queries:
        a, b, k = query
        if (a<1) or (a>b) or (b>n) or (k < 0) or (k > 1000):
            return -1
        arr[a-1] += k
        if b < n:
            arr[b] -= k
    
    max_val = 0
    running_total = 0
    for val in arr:
        running_total += val
        if running_total > max_val:
            max_val = running_total
    
    return max_val
