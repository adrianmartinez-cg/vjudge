from collections import deque

def isValidMove(i,j,n,m,visited):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return False
    if visited[i][j]:
        return False
    return True

def getNeighbors(i,j,n,m,visited):
    neighbors = []
    diffRow = [-1,1,0,0]
    diffCol = [0,0,-1,1]
    for k in range(len(diffRow)):
        if isValidMove(i+diffRow[k],j+diffCol[k],n,m,visited):
            neighbors.append((i+diffRow[k],j+diffCol[k]))
    return neighbors

def bfs(i,j,n,m,visited,finalPos,lastMove):
    q = deque()
    found = False
    q.append((i,j))
    while len(q) > 0:
        vi,vj = q.popleft()
        visited[vi][vj] = True
        for neighbor in getNeighbors(vi,vj,n,m,visited):
            ni,nj = neighbor
            if not visited[ni][nj]:
                direction = (ni-vi,nj-vj)
                lastMove[neighbor] = (vi,vj)
                q.append(neighbor)
                if neighbor == finalPos:
                    found = True
                    q = deque()
                    break
    return found
    
n,m = list(map(int,input().split()))
visited = [[False for j in range(m)] for i in range(n)]
lastMove = {}
initPos = (0,0)
finalPos = (0,0)
for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j] == "*":
            visited[i][j] = True
        elif row[j] == "S":
            initPos = (i,j)
        elif row[j] == "T":
            finalPos = (i,j)
found = bfs(initPos[0],initPos[1],n,m,visited,finalPos,lastMove)
v = finalPos
turns = deque([(0,0)])
if len(lastMove) > 0 and found:
    while v != initPos:
        u = lastMove[v]
        direction = (u[0]-v[0],u[1]-v[1])
        lastDirection = turns[-1]
        if direction != lastDirection:
            turns.append(direction)
        v = lastMove[v]
        if len(turns) > 4: break
    if len(turns) <= 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")