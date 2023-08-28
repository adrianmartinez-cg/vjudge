n,q = list(map(int,input().split()))
A = list(map(int,input().split()))
Amax = -1
maxPos = -1
for i in range(len(A)):
    if A[i] > Amax:
        Amax = A[i]
        maxPos = i
queries = []
queriesUnsorted = []
d = {}
maxQuery = 0
for i in range(q):
    m = int(input())
    query = (m,i+1)
    queries.append(query)
    queriesUnsorted.append(query)
    d[query] = ""
    if m > maxQuery: maxQuery = m
queries.sort()
k = 0
l = 0
r = 1
lastQ = 0
lastR = 0

if q > 0:
    for i in range(min(n,maxQuery)):
        queryNum = i + 1
        left , right = A[l] , A[r]
        if left == Amax:
            lastQ = queryNum
            lastR = r
            break
        if left > right:
            A.append(right)
            A[r] = left
        else:
            A.append(left)
        nextQ = queries[k]
        nextQNum = nextQ[0]
        while queryNum == nextQNum:
            d[nextQ] = f"{left} {right}"
            k += 1
            if k < len(queries):
                nextQ = queries[k]
                nextQNum = nextQ[0]
            else:
                break
        l += 1
        r += 1
    elemsLeft = len(A) - lastQ
    for i in range(k,len(queries)):
        query = queries[i]
        m = query[0] 
        r = lastR + (m - lastQ) % elemsLeft
        right = A[r]
        d[query] = f"{left} {right}"
    for i in range(len(queriesUnsorted)):
        query = queriesUnsorted[i]
        print(d[query])