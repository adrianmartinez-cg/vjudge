import heapq
import io, os

def djikstra(adj,n,origin,heap):
    distance = [float('inf')] * (n+1)
    distance[origin] = 0
    while len(heap) > 0:
        dist,u = heapq.heappop(heap)
        if dist > distance[u]:
            continue
        for v,w in adj[u]:
            oldDist = distance[v]
            newDist = distance[u] + w
            if oldDist > newDist:
                distance[v] = newDist
                heapq.heappush(heap,(newDist,v))
    return distance

def initialize(n,origin):
    heap = []
    for i in range(1,n+1):
        if (i == origin): heapq.heappush(heap,(0,i))
        else: heapq.heappush(heap,(float('inf'),i))
    return heap

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n,m = map(int,input().decode().split())
adj = [[] for _ in range(n+1)]
adjReverse = [[] for _ in range(n+1)]
heap,heapReverse = initialize(n,1),initialize(n,n)
edges = []
for _ in range(m):
    a,b,c = map(int,input().decode().split())
    adj[a].append((b,c))
    adjReverse[b].append((a,c))
    edges.append((a,b,c))
distanceDirect = djikstra(adj,n,1,heap)
distanceReverse = djikstra(adjReverse,n,n,heapReverse)
smallestPrice = int(2e14) + 1
for i in range(len(edges)):
    a,b,c = edges[i]
    distToA = distanceDirect[a]
    distToB = distanceReverse[b]
    priceWithDiscount = c // 2
    totalPrice = distToA + distToB + priceWithDiscount
    if totalPrice < smallestPrice:
        smallestPrice = totalPrice
print(smallestPrice)