from collections import defaultdict
from collections import deque

def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(u,visited):
    s = deque()
    component = []
    colors = {}
    s.append(u)
    maxOccur = 0
    predColor = 0
    while len(s) > 0:
        v = s.pop()
        color = C[v-1]
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        numOccur = colors[color]
        if numOccur > maxOccur:
            maxOccur = numOccur
            predColor = color
        component.append(v)
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                s.append(neighbor)
                visited[neighbor] = True
    return component,predColor

def connectedComponents():
    visited = [False] * (n + 1)
    components = []
    for vertex in graph:
        if not visited[vertex]:
            component,predColor = dfs(vertex, visited)     
            components.append((component,predColor))
    return components

n,m,k = map(int,input().split())
C = list(map(int,input().split()))
graph = defaultdict(list)

for _ in range(m):
    u,v = map(int,input().split())
    addEdge(u,v)
components = connectedComponents()
numPaintings = 0
for component in components:
    socks = component[0]
    predColor = component[1]
    for s in socks:
        color = C[s-1]
        if color != predColor:
            numPaintings += 1
print(numPaintings)