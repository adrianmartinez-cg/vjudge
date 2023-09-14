def fastPowMod(a,b,m):
    a %= m
    c = 1
    while b > 0:
        if b % 2 == 1:
            c = (c * a) % m
        a = (a * a) % m
        b //= 2
    return c

p = int(1e7 + 7)
out = []
while True:
    n,k = list(map(int,input().split()))
    if (n,k) == (0,0): break
    exp1 = fastPowMod(n,k,p)
    exp2 = 2 * fastPowMod(n-1,k,p)
    exp3 = fastPowMod(n,n,p)
    exp4 = 2* fastPowMod(n-1,n-1,p)
    exps = [exp1,exp2,exp3,exp4]
    exp = 0
    for x in exps:
        exp += x
        exp %= p
    out.append(exp)
for ans in out:
    print(ans)