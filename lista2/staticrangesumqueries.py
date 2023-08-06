def accumulativeSum(A):
    for i in range(1,len(A)):
        A[i] += A[i-1]

def calcSumInRange(A,l,r):
    subtract = 0
    if l > 1:
        subtract = A[l-2]
    return A[r-1] - subtract

n,q = list(map(int,input().split()))
A = list(map(int,input().split()))
accumulativeSum(A)
sums = []
for _ in range(q):
    l,r = list(map(int,input().split()))
    sums.append(calcSumInRange(A,l,r))
for val in sums:
    print(val)