n = int(input())
k = list(map(int,input().split()))
u = {}
maxLen = 0
currentLen = 0
for i in range(n):
    if k[i] not in u:
        u[k[i]] = i
        currentLen += 1
    else:
        currentLen = i - u[k[i]]
        u[k[i]] = i
    if currentLen > maxLen:
        maxLen = currentLen
print(maxLen)