def fastPowMod(a,b,m):
    a %= m
    c = 1
    while b > 0:
        if b % 2 == 1:
            c = (c * a) % m
        a = (a * a) % m
        b >>= 1
    return c

p = int(1e7 + 7)
out = []
# calcular [n ^ k + 2(n-1)^k + n ^ n + 2(n-1)^n-1] mod p
while True:
    n,k = list(map(int,input().split()))
    if (n,k) == (0,0): break
    exp1 = fastPowMod(n,k,p)
    exp2 = (2 * fastPowMod(n-1,k,p))%p
    exp3 = fastPowMod(n,n,p)
    exp4 = (2* fastPowMod(n-1,n-1,p))%p
    exp = ((exp1+exp2)%p + (exp3+exp4)%p)%p
    out.append(exp)
for _ in out:
    print(_)