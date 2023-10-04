import heapq

def djikstra(adj,n,origin,heap):
    distance = [float('inf')] * (n+1)
    distance[origin] = 0

    for i in range(n):
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
    return distance[n]

def initialize(n,k,P):
    addWeight = {}
    heap = []
    adj = {}
    for i in range(1,n+1):
        addWeight[i] = 0
        heap.append((float('inf'),i))
        adj[i] = {}
    heap[0] = (0,1)
    for v in P:
        addWeight[v] = k 
    return addWeight,heap,adj

def updateWeight(x,y,w,adj,addWeight):
    wy = w + addWeight[y]
    if y not in adj[x]:
        adj[x][y] = wy
    else:
        if wy < adj[x][y]:
            adj[x][y] = wy
        
n,m,t,k,p = map(int,input().split())
t *= 60
P = []
if p > 0:
    P = list(map(int,input().split()))
addWeight,heap,adj = initialize(n,k,P)
for _ in range(m):
    x,y,w = map(int, input().split())
    w *= 60
    updateWeight(x,y,w,adj,addWeight)
timeToInn = djikstra(adj,n,1,heap)
if timeToInn <= t:
    print(timeToInn)
else:
    print(-1)