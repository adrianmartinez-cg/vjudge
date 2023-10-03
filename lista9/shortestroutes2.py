def floydWarshall(adj):
    m = len(adj)
    dist = [[float('inf')] * m for _ in range(m)]
    for i in range(1,m):
        for j in range(1,m):
            if i == j:
                dist[i][j] = 0
            elif adj[i][j] != 0:
                dist[i][j] = adj[i][j]
    for k in range(1,m):
        for i in range(1,m):
            for j in range(1,m):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n,m,q = map(int,input().split())
adj = [[float('inf')] * (n+1) for _ in range(n+1)]
for j in range(1,n+1):
    adj[j][j] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if c < adj[a][b]:
        adj[a][b] = c
        adj[b][a] = c
distMatrix = floydWarshall(adj)
dists = []
for _ in range(q):
    a,b = map(int,input().split())
    if distMatrix[a][b] == float('inf'): 
        dists.append(-1)
    else:
        dists.append(distMatrix[a][b])
for d in dists:
    print(d)