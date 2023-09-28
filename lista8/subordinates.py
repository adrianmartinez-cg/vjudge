import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getNeighbors(self,u):
        return self.graph[u]
     
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)
 
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack # normalmente seria o inverso da stack, mas queremos subir das folhas para a raiz , n o contrario

sys.setrecursionlimit(10**6)
n = int(input())
A = list(map(int,input().split()))
g = Graph(n)
numSubs = [0]*n
for i in range(len(A)):
    g.addEdge(A[i]-1,i+1)
topOrder = g.topologicalSort()
for k in topOrder:
    neighbors = g.getNeighbors(k)
    for m in neighbors:
        numSubs[k] += 1 + numSubs[m]
out = ""
for i in range(n):
    out += f"{numSubs[i]}"
    if i < n: out += " "
print(out)