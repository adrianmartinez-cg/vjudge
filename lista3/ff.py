n,q = list(map(int,input().split()))
ans = []
g = {}
for _ in range(q):
    t,a,b = list(map(int,input().split()))
    if t == 1:
        if a not in g:
            g[a] = set()
            g[a].add(b)
        else:
            g[a].add(b)
    if t == 2:
        if a in g:
            g[a].discard(b)
    if t == 3:
        x = 'No'
        if a in g and b in g:
            if b in g[a] and a in g[b]:
                x = 'Yes'
        ans.append(x)
for _ in ans:
    print(_)