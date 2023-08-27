n,q = list(map(int,input().split()))
A = list(map(int,input().split()))
Amax = max(A)
maxPos = A.index(Amax)
queries = []
d = {}
maxQuery = 0
for i in range(q):
    m = int(input())
    queries.append((m,i+1))
    d[i+1] = ""
    if m > maxQuery: maxQuery = m
queries.sort()
k = 0
l = 0
r = 1
lastQ = 0
lastR = 0

if q > 0:
    for i in range(min(n,maxQuery)):
        nextQ = queries[k][0]
        left , right = A[l] , A[r]
        if left == Amax:
            lastQ = i + 1
            lastR = r
            break
        if left > right:
            A.append(right)
            A[r] = left
        else:
            A.append(left)
        if i + 1 == nextQ:
            d[k+1] = f"{left} {right}"
            k += 1
        l += 1
        r += 1
    elemsLeft = len(A) - lastQ
    for i in range(k,len(queries)):
        m = queries[i][0] 
        r = lastR + (m - lastQ) % elemsLeft
        right = A[r]
        d[i+1] = f"{left} {right}"
    for i in range(len(queries)):
        query = queries[i][1]
        print(d[query])