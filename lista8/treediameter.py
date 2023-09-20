import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.maxDist = -1
        self.lastVisited = -1
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited,traversal,distance):
        if distance > self.maxDist:
            self.maxDist = distance
            self.lastVisited = v
        visited.add(v)
        traversal.append(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited,traversal,distance + 1)
 
    def DFS(self, v):
        visited = set()
        traversal = []
        self.DFSUtil(v, visited,traversal,0)
        return traversal

sys.setrecursionlimit(2*100000) 
n = int(input())
g = Graph(n)
lastV = -1
for _ in range(n-1):
    u,v = [int(i) for i in input().split()]
    g.addEdge(u-1,v-1)
    g.addEdge(v-1,u-1)
    lastV = u-1
g.DFS(lastV)
dist1 = g.maxDist
g.maxDist = -1
g.DFS(g.lastVisited)
dist2 = g.maxDist
print(dist2)