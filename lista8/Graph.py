from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self,u):
        s = deque()
        visited = [False] * self.V
        traversal = []
        s.append(u)
        while len(s) > 0:
            v = s.pop()
            traversal.append(v)
            visited[v] = True
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    s.append(neighbor)
        return traversal

    def bfs(self,u):
        q = deque()
        visited = [False] * self.V
        traversal = []
        q.append(u)
        while len(q) > 0:
            v = q.popleft()
            traversal.append(v)
            visited[v] = True
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    q.append(neighbor)
        return traversal
    
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
 
        return stack[::-1]  
    
    def isCyclicUtil(self, v, visited, recStack):
 
        visited[v] = True
        recStack[v] = True
 
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[v] = False
        return False
 
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False