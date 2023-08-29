import math

n,k = list(map(int,input().split()))
d = []
q = []
out = -1
intRoot = math.isqrt(n)
hasExactRoot = intRoot == math.sqrt(n)
for i in range(1,intRoot+1):
    if n % i == 0:
        div = n // i
        d.append(i)
        if not hasExactRoot:
            q.append(div)
        elif hasExactRoot and i != intRoot:
            q.append(div)       
for i in range(len(q)-1,-1,-1):
    d.append(q[i])
if k <= len(d):
    out = d[k-1]
print(out)