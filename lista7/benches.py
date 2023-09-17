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

def P(n,r,f):
    fn = f[n]
    fnr = f[n-r]
    return fn // fnr

n = int(input())
numBenches = 5
f = fact(5)
count = 1
for i in range(n,n-numBenches,-1):
    count *= i ** 2
count = count // f[numBenches]
print(count)