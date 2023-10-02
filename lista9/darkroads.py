m,n = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n):
    a,b,w = map(int, input().split())
    adj[a].append((b,w))
    adj[b].append((a,w))
a,b = map(int, input().split()) # inutil