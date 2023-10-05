from collections import defaultdict
from collections import deque

def init(n):
    for i in range(1,n+1):
        parent[i] = i
        size[i] = 1

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    if a != b:
        if size[a] < size[b]: 
            a,b = b,a
        parent[b] = a
    size[a] += size[b]

def dfs(u,visited):
        s = deque()
        component = []
        s.append(u)
        while len(s) > 0:
            v = s.pop()
            component.append(v)
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    s.append(neighbor)
                    visited[neighbor] = True
        return component

def connectedComponents():
    visited = [False] * (n + 1)
    components = []
    for vertex in graph:
        if not visited[vertex]:
            component = dfs(vertex, visited)     
            components.append(component)
    return components

def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def initializeGraph():
    for i in range(1,n+1):
        foo = graph[i] # só para inicializar as listas do dict

def isNotSubordinate(v):
    return v not in sup

n = int(input())
parent = [0] * (n+1)
size = [0] * (n+1)
sup = {}
Q = list(map(int,input().split()))
m = int(input())
graph = defaultdict(list)
initializeGraph()
# kruskal
init(n)
edges = []
mstSum = 0
for i in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))
edges.sort()
for w,u,v in edges:
    pu,pv = find(u),find(v)
    if pu != pv and isNotSubordinate(v): 
        # se estão em componentes diferentes, 
        # e v não tem superior
        addEdge(u,v)
        mstSum += w
        union(pu,pv)
        sup[v] = u
components = connectedComponents()
if len(components) == 1:
    print(mstSum)
else:
    print(-1)