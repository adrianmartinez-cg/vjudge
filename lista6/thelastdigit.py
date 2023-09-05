def fastPowMod(a,b,m):
    a %= m
    c = 1
    while b > 0:
        if b % 2 == 1:
            c = (c * a) % m
        a = (a * a) % m
        b //= 2
    return c

t = int(input())
out = []
for _ in range(t):
    a,b = list(map(int,input().split()))
    out.append(fastPowMod(a,b,10))
for _ in out:
    print(_)