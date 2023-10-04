from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def getNeighbors(self,u):
        return self.graph[u]

    def findCycle(self):
        unvisited = set()
        visiting = set()
        visited = set()
        parent = {}
        for i in range(self.V):
            unvisited.add(i)
            parent[i] = -1
        while len(unvisited) > 0:
            current = unvisited.pop()
            path = self.dfs(current,unvisited,visiting,visited,parent)
            if len(path) > 0:
                return path
        return []
    
    def dfs(self,current,unvisited,visiting,visited,parent):
        self.moveVertex(current,unvisited,visiting)
        for neighbor in self.getNeighbors(current):
            parent[neighbor] = current
            if neighbor in visited:
                continue
            if neighbor in visiting:
                path = self.getPath(current,neighbor,parent)
                return path
            if self.dfs(neighbor,unvisited,visiting,visited,parent):
                path = self.getPath(current,neighbor,parent)
                return path
        self.moveVertex(current,visiting,visited)

    def moveVertex(self,current,sourceSet,destinationSet):
        sourceSet.discard(current)
        destinationSet.add(current)
    
    def getPath(self,current,start,parent):
        path = []
        node = current
        while node != start:
            path.append(node)
            node = parent[node]
        path.append(start)
        return path

n,m = list(map(int,input().split()))
g = Graph(n)
for _ in range(m):
    u,v = list(map(int,input().split()))
    u,v = u-1,v-1
    g.addEdge(u,v)
    g.addEdge(v,u)
cycle = g.findCycle()
if cycle == -1:
    print("IMPOSSIBLE")
else:
    out = ""
    for i in range(len(cycle)):
        out += f"{cycle[i]+1}"
        if i < n - 1:
            out += " "
    print(len(cycle))
    print(out)