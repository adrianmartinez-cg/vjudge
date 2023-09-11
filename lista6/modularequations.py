import math

def findDivisors(n):
    d = []
    q = []
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
    return d

a,b = list(map(int,input().split()))
out = "infinity"
count = 0
if a > b: # se a = b , n pode assumir qualquer valor
    c = a - b # se a ≡ b (mod x), (a-b) ≡ 0 (mod x)
    ds = findDivisors(c)
    for d in ds:
        if a % d == b:
            count += 1
if a != b:
    out = count
print(out)