from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,visited):
        s = deque()
        component = []
        s.append(u)
        while len(s) > 0:
            v = s.pop()
            component.append(v)
            visited[v] = True
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    s.append(neighbor)
                    visited[neighbor] = True
        return component

    def connectedComponents(self):
        visited = [False] * (self.V + 1)
        components = []
        for vertex in self.graph:
            if not visited[vertex]:
                component = self.dfs(vertex, visited)     
                components.append(component)
        return components

    def checkComponent(self,component):
        size = len(component)
        isCompleteGraph = True
        for v in component:
            if len(self.graph[v]) < size - 1:
                isCompleteGraph = False
                break
        return isCompleteGraph
    
n,m = map(int,input().split())
g = Graph(n)
for _ in range(m):
    a,b = map(int,input().split())
    g.addEdge(a,b)
components = g.connectedComponents()
reasonableGraph = True
for c in components:
    isCompleteGraph = g.checkComponent(c)
    if not isCompleteGraph: 
        reasonableGraph = False
        break
if reasonableGraph:
    print('YES')
else:
    print('NO')