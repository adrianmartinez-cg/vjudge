def primeFactors(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i 
        i += 1
        if i * i  > n : break
    if n > 1:
        factors.append(n)
    return factors

t = int(input())
out = []
for _ in range(t):
    a,b,c,d = list(map(int,input().split()))
    abFactors = primeFactors(a*b)
    ans = "-1 -1"
    for x in range(a+1,c+1): 
        firstFactor = x
        y = 1
        for f in abFactors:
            if firstFactor % f == 0:
                firstFactor //= f
            else:
                y *= f
        m = 1
        while (m*y) <= b:
            m += 1
        if (m*y) <= d:
            ans = f"{x} {m*y}"
            break
    out.append(ans)
for _ in out:
    print(_)