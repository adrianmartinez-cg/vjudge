import heapq

def djikstra(adj,origin,pred,heap):
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

def printAnswer(path):
    ans = " ".join(map(str, reversed(path)))
    print(ans)

def findPath(pred):
    path = [n]
    i = n
    while(i != 1):
        if pred[i] == 0:
            return [-1] 
        path.append(pred[i])
        i = pred[i]
    return path

def initialize(n):
    pred = {}
    heap = []
    for i in range(1,n+1):
        pred[i] = 0
        heap.append((float('inf'),i))
    heap[0] = (0,1)
    return pred,heap

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
pred,heap = initialize(n)
for _ in range(m):
    a,b,w = map(int, input().split())
    adj[a].append((b,w))
    adj[b].append((a,w))
djikstra(adj,1,pred,heap)
path = findPath(pred)
printAnswer(path)