def maxCandies(X,n):
    a,b = 1,1
    c = 0 
    A,B = 0,0 # peso dos doces
    l = 0
    r = n - 1
    checkA , checkB = True,True 
    while l < r:
        if checkA:
            A += X[l]
            checkA = False
        if checkB:
            B += X[r]
            checkB = False
        if A < B:
            l += 1
            a += 1
            checkA = True
        elif A == B:
            c = a + b
            l += 1
            a += 1
            checkA = True
        elif A > B:
            r -= 1
            b += 1
            checkB = True
    return c

t = int(input())
C = []

for _ in range(t):
    n = int(input())
    X = list(map(int,input().split()))
    C.append(maxCandies(X,n))
for _ in C:
    print(_)