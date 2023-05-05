def arrayManipulation(n, a, b, k):
    # initialize the array
    arr = [0] * n
    
    # update the array based on the queries
    for i in range(len(a)):
        arr[a[i]-1] += k[i]
        if b[i] < n:
            arr[b[i]] -= k[i]
    
    # calculate the maximum value in the array
    max_val = 0
    running_total = 0
    for val in arr:
        running_total += val
        if running_total > max_val:
            max_val = running_total
    
    return max_val



# 2 metode functionale
# 3 structurale (statement, branch, circuite)
# 2 mutanti de omorat