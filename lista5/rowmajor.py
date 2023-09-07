import math

def nextChar(c):
    return chr(ord(c) + 1)

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
    d.pop()
    return d

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    d = findDivisors(n)
    s = list("a"*n)
    for i in range(len(s)):
        for f in d:
            if i + f < len(s):
                if s[i] == s[i+f]:
                    s[i+f] = nextChar(s[i])
    out.append("".join(s))
for _ in out:
    print(_)
