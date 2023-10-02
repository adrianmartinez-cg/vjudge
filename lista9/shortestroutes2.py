import heapq
 
def initialize(n,origin):
    pred = {}
    heap = []
    for i in range(1,n+1):
        pred[i] = 0
        dist = float('inf')
        if i == origin: dist = 0
        heapq.heappush(heap,(dist,i))
    return pred,heap
 
def djikstra(adj,origin,destination,pred,heap):
    n = len(adj)
    distance = [float('inf')] * n
    distance[origin] = 0
 
    for i in range(1,n):
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
    return distance[destination]
 
n,m,q = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
dist = []
for _ in range(q):
    a,b = map(int,input().split())
    pred,heap = initialize(n,a)
    dist.append(djikstra(adj,a,b,pred,heap))
for d in dist:
    if d == float('inf'): 
        print(-1)
    else: 
        print(d)