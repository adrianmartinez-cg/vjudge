def maxSubArraySum(A,n):
    maxCurrent = A[0]
    maxSum = maxCurrent
    for i in range(1,n):
        maxCurrent = max(A[i],A[i]+ maxCurrent)
        if maxCurrent > maxSum:
            maxSum = maxCurrent
    return maxSum

n = int(input())
A = list(map(int,input().split()))
print(maxSubArraySum(A,n))