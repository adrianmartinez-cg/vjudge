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
        maxSize = 0
        for vertex in self.graph:
            if not visited[vertex]:
                component = self.dfs(vertex, visited)
                components.append(component)
                if len(component) > maxSize:
                    maxSize = len(component)    
        return len(components),maxSize


n,m = map(int,input().split())
g = Graph(n)
out = []
for _ in range(m):
    u,v = map(int,input().split())
    g.addEdge(u,v)
    components,maxSize = g.connectedComponents()
    out.append(f"{components} {maxSize}")
for _ in out:
    print(_)