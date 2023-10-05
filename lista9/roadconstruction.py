from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        for i in range(1,vertices+1):
            init = self.graph[i] # só para inicializar as listas do dict

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def init(n):
    for i in range(1,n+1):
        parent[i] = i
        size[i] = 1

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    global maxSize
    if a != b:
        if size[a] < size[b]: 
            a,b = b,a
        parent[b] = a
    size[a] += size[b]
    if size[a] > maxSize:
        maxSize = size[a]

maxSize = 1
n,m = map(int,input().split())
parent = [0] * (n+1) # ancestral do vertice
uniqueParents = set()
size = [0] * (n+1)
g = Graph(n)
edges = []
numComponents = n

for _ in range(m):
    u,v = map(int,input().split())
    edges.append((u,v))
    g.addEdge(u,v)

init(n)
out = []
for u,v in edges:
    u,v = find(u),find(v)
    if u != v:
        union(u,v)
        numComponents -= 1
        ans = f"{numComponents} {maxSize}"
    out.append(ans)
for _ in out:
    print(_)