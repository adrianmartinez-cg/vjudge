from collections import deque
 
a,b = list(map(int,input().split()))
visited = {}
q = deque([a])
while len(q) > 0:
    v = q.popleft()
    w = 2*v
    x = 10*v + 1
    if w not in visited and w <= b:
        q.append(w)
        visited[w] = v
    if x not in visited and x <= b:
        q.append(x)
        visited[x] = v
path = [b]
if b not in visited:
    print("NO")
else:
    print("YES")
    node = b
    while node > a:
        node = visited[node]
        path.append(node)
    print(len(path))
    out = ""
    for i in range(len(path)-1,-1,-1):
        out += f"{path[i]}"
        if i > 0:
            out += " "
    print(out)