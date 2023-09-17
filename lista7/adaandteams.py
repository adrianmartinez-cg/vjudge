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

def solve(n,a,b,d,p,fact):
    # [C(B,D) ^ (A) * C(N,A)] % p = ((C(B,D)%p)^A % p) * C(N,A)%p
    return fastPowMod(C(b,d,p,fact),a,p) * C(n,a,p,fact)%p

out = []
p = int(1e9+7)
f = factMod(10**6,p)
while True:
    try:
        n,a,b,d = list(map(int,input().split()))
        out.append(solve(n,a,b,d,p,f))
    except:
        break
for _ in out:
    print(_)