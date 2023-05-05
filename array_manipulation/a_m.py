import math
import os
def arrayManipulation(n, queries):
    arr = [0] * n

    if (n < 3) or (n > math.pow(10,7)):
        return -1    
    for query in queries:
        a, b, k = query
        if not ((1<=a) and (a<=b) and (b<=n)):
            return -1
        if (k < 0) or (k > math.pow(10,9)):
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
