def addQueryToResults(query,queryResults,wins,additional):
    queryFormatted = (query[1],query[0])
    if queryFormatted not in queryResults:
        queryResults[queryFormatted] = []
    queryResults[queryFormatted].append(wins[query[1]]+additional)

t = int(input())
out = []
for _ in range(t):
    n,q = list(map(int,input().split()))
    aStr = input().split()
    A = []
    wins = {}
    queryResults = {}
    Amax = 0
    AmaxIndex = 0
    for i in range(len(aStr)):
        A.append((i+1,int(aStr[i])))
        wins[i+1] = 0
        if int(aStr[i]) > Amax: 
            Amax = int(aStr[i])
            AmaxIndex = i + 1
    queriesUnsorted = []
    queries = []
    maxK = 0
    for _ in range(q):
        i,k = list(map(int,input().split()))
        if k > maxK: maxK = k
        queriesUnsorted.append((i,k))
        queries.append((k,i))
    queries.sort()
    j = 0
    l = 0
    r = 1
    lastround = 0
    lastr = 0
    for i in range(min(maxK,n)):
        left,right = A[l],A[r]
        leftVal,rightVal = left[1],right[1]
        if leftVal == Amax:
            winnerIndex = left[0]
            wins[winnerIndex] += 1
            lastround = i + 1
            lastr = r
            break
        if leftVal < rightVal:
            smaller = left
            winnerIndex = right[0]
            wins[winnerIndex] += 1
        elif leftVal > rightVal:
            A[r] = left
            smaller = right
            winnerIndex = left[0]
            wins[winnerIndex] += 1
        A.append(smaller)
        l += 1
        r += 1
        round = i + 1
        nextQuery = queries[j]
        while round == nextQuery[0]:
            addQueryToResults(nextQuery,queryResults,wins,0)
            j += 1
            if j < len(queries):
                nextQuery = queries[j]
    for i in range(j,len(queries)):
        query = queries[i]
        round , participant = query[0] , query[1]
        additionalWins = 0
        if participant == AmaxIndex:
            additionalWins = round - lastround
        addQueryToResults(query,queryResults,wins,additionalWins)
    nextIndexInQueryResults = {}
    for i in range(len(queriesUnsorted)):
        query = queriesUnsorted[i]
        if query not in nextIndexInQueryResults:
            index = 0
        else:
            index = nextIndexInQueryResults[query]
        out.append(queryResults[query][index])
        nextIndexInQueryResults[query] = index + 1
for _ in out:
    print(_)