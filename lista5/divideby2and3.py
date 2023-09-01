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

n = int(input())
A = list(map(int,input().split()))
minX = 999 # n = 2^x*3^y*M
minY = 999
numOps = -1
valid = True
for i in range(n):
    num = A[i]
    numFact = (0,0,1)
    j = 2
    while num > 1:
        while num % j == 0:
            num //= j
            if j == 2: numFact = (numFact[0]+1,numFact[1],1)
            elif j == 3: numFact = (numFact[0],numFact[1]+1,1)
        j += 1
        if j > 3: break
    if num > 1:
        numFact = (numFact[0],numFact[1],num)
    if i > 0:
        prevNumFact = A[i-1]
        if prevNumFact[2] != numFact[2]: 
            valid = False
            break
    x,y = numFact[0],numFact[1]
    if x < minX: minX = x
    if y < minY: minY = y
    A[i] = numFact
if valid:
    numOps = 0
    for i in range(n):
        x,y = A[i][0],A[i][1]
        diffX = x - minX 
        diffY = y - minY
        numOps += diffX + diffY
print(numOps)