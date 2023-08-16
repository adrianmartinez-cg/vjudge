n = int(input())
k = list(map(int,input().split()))
u = {}
maxLen = 0
for i in k:
    if i not in u:
        u[i] = 1
    else:
        u = {}
        u[i] = 1
    l = len(u)
    if l > maxLen:
        maxLen = l
print(maxLen)