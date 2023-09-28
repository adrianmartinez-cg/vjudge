n,m = list(map(int,input().split()))
g = {}
for _ in range(m):
    u,v = list(map(int,input().split()))
    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)
    if v not in g:
        g[v] = [u]
    else:
        g[v].append(u)
