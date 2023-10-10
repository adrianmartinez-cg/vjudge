import heapq

def djikstra(adj,n,origin,heap):
    distance = [float('inf')] * (n+1)
    distance[origin] = 0
    while len(heap) > 0:
        dist,u = heapq.heappop(heap)
        if dist > distance[u]:
            continue
        for v in adj[u]:
            w = adj[u][v]
            oldDist = distance[v]
            newDist = distance[u] + w
            if oldDist > newDist:
                distance[v] = newDist
                heapq.heappush(heap,(newDist,v))
    return distance

def initialize(n,origin,end):
    adj = {}
    adjReverse = {}
    heap = []
    heapReverse = []
    for i in range(1,n+1):
        adj[i] = {}
        adjReverse[i] = {}
        heap.append((float('inf'),i))
        heapReverse.append((float('inf'),i))
    heap[origin-1] = (0,origin)
    heapReverse[end-1] = (0,end)
    return adj,adjReverse,heap,heapReverse

d = int(input())
paths = []
for _ in range(d):
    n,m,k,s,t = map(int,input().split())
    adj,adjReverse,heap,heapReverse = initialize(n,s,t)
    for _ in range(m):
        u,v,w = map(int,input().split())
        adj[u][v] = w
        adjReverse[v][u] = w
    distance = djikstra(adj,n,s,heap)
    distanceReverse = djikstra(adjReverse,n,t,heapReverse)
    pathLength = distance[t]
    for _ in range(k):
        u,v,w = map(int,input().split())
        newDistDirect = distance[u] + w + distanceReverse[v]
        newDistReverse = distance[v] + w + distanceReverse[u]
        newDist = min(newDistDirect,newDistReverse)
        if newDist < pathLength:
            pathLength = newDist
    paths.append(pathLength)
for p in paths:
    if p == float('inf'):
        print(-1)
    else:
        print(p)