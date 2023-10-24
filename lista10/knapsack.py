import math

def toString(items):
    string = ""
    for i in range(len(items)-1,-1,-1):
        string += str(items[i])
        if i > 0:
            string += " "
    return string

t = int(input())
out = []
for _ in range(t):
    n,capacity = map(int,input().split())
    weights = list(map(int,input().split()))
    W = []
    for i in range(len(weights)):
        W.append((weights[i],i))
    W.sort(reverse=True)
    items = []
    numItems = 0
    totalWeight = 0
    for i in range(len(W)):
        w = W[i][0]
        j = W[i][1]
        if totalWeight + w <= capacity:
            totalWeight += w
            numItems += 1
            items.append(j+1)
        else:
            continue
    if numItems > 0 and totalWeight >= math.ceil(capacity/2):
        out.append(numItems)
        out.append(toString(items))
    else:
        out.append(-1)
for _ in out:
    print(_)