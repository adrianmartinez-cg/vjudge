import heapq

def djikstra(adj,n,origin,heap,pred):
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
                pred[v] = u
                distance[v] = newDist
                heapq.heappush(heap,(newDist,v))
    return distance[n]

def initialize(n):
    heap = []
    pred = {}
    for i in range(1,n+1):
        pred[i] = 0
        heap.append((float('inf'),i))
    heap[0] = (0,1)
    return heap,pred

def findPath(pred):
    path = [n]
    i = n
    while(i != 1):
        if pred[i] == 0:
            return [-1] 
        path.append(pred[i])
        i = pred[i]
    return path[::-1]

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
heap,pred = initialize(n)
edgesWeight = {}
for _ in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    edgesWeight[(a,b)] = c
normalRoute = djikstra(adj,n,1,heap,pred)
shortestPath = findPath(pred)
edgeMaxWeight = 0
for i in range(len(shortestPath)-1):
    edge = (shortestPath[i],shortestPath[i+1])
    w = edgesWeight[edge]
    if w > edgeMaxWeight:
        edgeMaxWeight = w
discountRoute = normalRoute - edgeMaxWeight + (edgeMaxWeight // 2)
print(discountRoute)