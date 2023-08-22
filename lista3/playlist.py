n = int(input())
k = list(map(int,input().split()))
u = {}
currentLen = 0 
maxLen = 0
last = 0
for i in range(n):
    if k[i] not in u:
        u[k[i]] = i
    else:
        if u[k[i]] >= last:
            last = u[k[i]] + 1
        u[k[i]] = i
    currentLen = i - last + 1
    if currentLen > maxLen:
        maxLen = currentLen
print(maxLen)