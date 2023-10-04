#disjoint set union
def init(m):
    for i in range(m):
        parent[i] = i
        size[i] = 1

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a,b = find(a),find(b)
    if a != b:
        if size[a] < size[b]: a,b = b,a
        parent[b] = a
    size[a] += size[b]

maxLimit = int(2e5)
parent = [0] * maxLimit # ancestral do vertice
size = [0] * maxLimit # tamanho do componente q o vertice esta inserido
m,n = map(int,input().split())

#kruskal
while m != 0:
    init(m)
    edges = []
    mstSum = 0
    graphSum = 0
    for i in range(n):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    edges.sort()
    for w,u,v in edges:
        u,v = find(u),find(v)
        graphSum += w
        if u != v:
            mstSum += w
            union(u,v)
    maxEconomy = graphSum - mstSum
    print(maxEconomy)
    m,n = map(int,input().split())