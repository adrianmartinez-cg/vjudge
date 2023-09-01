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

def areCoprime(n1,n2):
    n1Factors = primeFactors(n1)
    areCoprime = True
    for f in n1Factors:
        if n2 % f == 0:
            areCoprime = False
            break
    return areCoprime

def sieve(n):
    primes = [True for i in range(n+1)]
    primeNums = []
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p,n+1,p):
                primes[i] = False
        p += 1
    for i in range(2,n+1):
        if primes[i]:
            primeNums.append(i)
    return primeNums

n = int(input())
A = list(map(int,input().split()))
k = 0
added = {}
primes = sieve(10**5) # esse valor foi um chute, n dá pra gerar todos os fatores até 10^9
for i in range(1,len(A)):
    checkCoprime = areCoprime(A[i],A[i-1])
    factor = -1
    if not checkCoprime:
        k += 1
        for p in primes:
            if A[i] % p != 0 and A[i-1] % p != 0:
                factor = p
                break
        added[i] = factor
print(k)
out = f"{A[0]} "
for i in range(1,len(A)):
    if i in added:
        out += f"{str(added[i])} "
    out += str(A[i])
    if i < len(A) - 1:
        out += " "
print(out)