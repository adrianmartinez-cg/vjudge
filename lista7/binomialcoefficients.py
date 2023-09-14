def fastPowMod(a,b,m):
    a %= m
    c = 1
    while b > 0:
        if b % 2 == 1:
            c = (c * a) % m
        a = (a * a) % m
        b >>= 1
    return c

def modInv(a,p):
    return fastPowMod(a,p-2,p)

def factMod(n,p):
    f = [1,1]
    for i in range(2,n+1):
        last = f[len(f)-1]
        f.append((i*last)%p)
    return f

def C(n,k,p,fact):
    return (fact[n] * (modInv(fact[k],p) % p) * (modInv(fact[n-k],p) % p)) % p

n = int(input())
p = int(1e9+7)
fact = factMod(10**6,p)
out = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    out.append(C(a,b,p,fact))
for _ in out:
    print(_)