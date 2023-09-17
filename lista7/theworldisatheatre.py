def fact(n):
    f = [1,1]
    for i in range(2,n+1):
        last = f[i-1]
        f.append((i*last))
    return f

def C(n,k,f):
    fn = f[n]
    fk = f[k]
    fnk = f[n-k]
    return fn // (fk * fnk)

n,m,t = list(map(int,input().split()))
f = fact(100)
minBoys = 4
count = 0
for numBoys in range(minBoys,t):
    numGirls = t - numBoys
    combBoys = C(n,numBoys,f)
    combGirls = C(m,numGirls,f)
    count += combBoys * combGirls
print(count)