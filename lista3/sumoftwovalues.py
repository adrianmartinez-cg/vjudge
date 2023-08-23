n,x = list(map(int,input().split()))
A = list(map(int,input().split()))
d = {}
r = "IMPOSSIBLE"
for i in range(n):
    d[A[i]] = i
for i in range(n):
    diff = x - A[i]
    if diff in d:
        if d[diff] != i:
            r = f"{i+1} {d[diff]+1}"
        break
print(r)