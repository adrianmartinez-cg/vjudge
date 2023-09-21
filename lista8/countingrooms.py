from collections import deque

def isValidMove(i,j,n,m,visited):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return False
    if visited[i][j]:
        return False
    return True

def getNeighbors(i,j,n,m,visited):
    neighbors = []
    up = (i-1,j)
    down = (i+1,j)
    left = (i,j-1)
    right = (i,j+1)
    if isValidMove(i-1,j,n,m,visited):
        neighbors.append(up)
    if isValidMove(i+1,j,n,m,visited):
        neighbors.append(down)
    if isValidMove(i,j-1,n,m,visited):
        neighbors.append(left)
    if isValidMove(i,j+1,n,m,visited):
        neighbors.append(right)
    return neighbors

def dfs(i,j,n,m,visited):
    s = deque()
    s.append((i,j))
    while len(s) > 0:
        vi,vj = s.pop()
        visited[vi][vj] = True
        for neighbor in getNeighbors(vi,vj,n,m,visited):
            ni,nj = neighbor
            if not visited[ni][nj]:
                s.append(neighbor)
    

n,m = list(map(int,input().split()))
visited = [[False for j in range(m)] for i in range(n)]
numRooms = 0
for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j] == "#":
            visited[i][j] = True
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            numRooms += 1
            dfs(i,j,n,m,visited)
print(numRooms)