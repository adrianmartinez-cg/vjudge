import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
     
    def DFSUtil(self, v, visited):

        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)
        return len(visited) - 1

sys.setrecursionlimit(10**6)
n = int(input())
A = list(map(int,input().split()))
g = Graph(n)
for i in range(len(A)):
    g.addEdge(A[i],i+2)
out = ""
for i in range(1,n+1):
    count = g.DFS(i)
    out += f"{count}"
    if i < n: out += " "
print(out)