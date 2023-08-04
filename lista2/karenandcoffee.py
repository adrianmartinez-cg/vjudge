def accumulativeSum(A):
    for i in range(1,len(A)):
        A[i] += A[i-1]

n,k,q = list(map(int,input().split()))
recDegrees = [0 for i in range(200000)]

for _ in range(n):
    l,r = list(map(int,input().split()))
    recDegrees[l-1] += 1
    if r <= 199999:
        recDegrees[r] -= 1

accumulativeSum(recDegrees)
for i in range(len(recDegrees)):
    if recDegrees[i] >= k:
        recDegrees[i] = 1
    else:
        recDegrees[i] = 0
accumulativeSum(recDegrees)

ans = []
for _ in range(q):
    a,b = list(map(int,input().split()))
    if a == 1:
        sum1 = 0 
    else:
        sum1 = recDegrees[a-2]
    sum2 = recDegrees[b-1]
    ans.append(sum2 - sum1)

for answer in ans:
    print(answer)