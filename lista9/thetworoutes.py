from collections import deque

def initialize():
    g = {}
    for i in range(1,n+1):
        g[i] = {}
    return g

def bfs(u,n,graph):
    q = deque()
    visited = set()
    parent = {}
    q.append(u)
    foundEndNode = False
    while len(q) > 0:
        v = q.popleft()
        visited.add(v)
        if v == n: 
            foundEndNode = True
            break
        for neighbor in graph[v]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = v 
    if foundEndNode:
        path = []
        currentNode = n
        while currentNode != u:
            path.append(currentNode)
            currentNode = parent[currentNode]
        path.append(u)
        return path  
    else:
        return []

n,m = map(int,input().split())
trainGraph = initialize()
busGraph = initialize()
for _ in range(m):
    a,b = map(int,input().split())
    trainGraph[a][b] = 1
    trainGraph[b][a] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and j not in trainGraph[i]:
            busGraph[i][j] = 1
            busGraph[j][i] = 1
bfsTrain = bfs(1,n,trainGraph)
bfsBus = bfs(1,n,busGraph)
if len(bfsTrain) == 0 or len(bfsBus) == 0:
    print(-1)
else:
    distA,distB = len(bfsTrain) -1 , len(bfsBus) - 1
    print(max(distA,distB))