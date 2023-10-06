def init(n):
    parent = []
    size = []
    adj = {}
    for i in range(n+1):
        parent.append(i)
        size.append(1)
        adj[i] = {}
    return parent,size,adj

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a,b = find(a),find(b)
    if a != b:
        if size[a] < size[b]: a,b = b,a
        parent[b] = a
    size[a] += size[b]

def dfs(i,p):
    global startVertex
    global foundCycle
    visited[i] = True
    traversal.append(i)
    for c in adj[i]:
        if visited[c] and c != p:
            traversal.append(c)
            startVertex = c
            foundCycle = True
            return
        if c != p and not visited[c]: dfs(c,i)
    if not foundCycle:
        traversal.pop()

def getCycle(c):
    cycle = []
    cycleEdges = []
    cycleStart = False
    for i in traversal:
        if i == c and cycleStart:
            cycle.append(i)
            break
        if i == c:
            cycleStart = True
        if cycleStart:
            cycle.append(i)
    for i in range(len(cycle)-1):
        edge = (cycle[i],cycle[i+1])
        cycleEdges.append(edgesId[edge])
    cycleEdges.sort()
    out = ""
    for i in range(len(cycleEdges)):
        out += f"{cycleEdges[i]}"
        if i < len(cycleEdges) - 1:
            out += " "
    return out
    
t = int(input())
cycles = []
for _ in range(t):
    n,m = map(int,input().split())
    edgesId = {}
    parentNode = {}
    parent,size,adj = init(n)
    cycle = "-1"
    foundCycle = False
    for i in range(m):
        u,v = map(int,input().split())
        edgesId[(u,v)] = (i+1)
        edgesId[(v,u)] = (i+1)
        adj[u][v] = 1
        adj[v][u] = 1
        parentNode[v] = u
        pu,pv = find(u),find(v)
        if pu != pv:
            union(u,v)
        else:
            if not foundCycle:
                visited = [False] * (n+1)
                traversal = []
                startVertex = 0
                dfs(v,u)
                cycle = getCycle(startVertex)          
    cycles.append(cycle)
for _ in cycles:
    print(_)