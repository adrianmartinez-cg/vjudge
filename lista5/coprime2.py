def primeFactors(n,factors):
    i = 2
    while n > 1:
        while n % i == 0:
            factors[i] = True
            n //= i 
        i += 1
        if i * i  > n : break
    if n > 1:
        factors[n] = True
    return factors

n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
factors = {}
for n in A:
    factors = primeFactors(n,factors)
coprimes = []
for k in range(1,m+1):
    isCoprime = True
    for f in factors:
        if k % f == 0:
            isCoprime = False
            break
    if isCoprime: coprimes.append(k)
print(len(coprimes))
for _ in coprimes:
    print(_)