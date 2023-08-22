n,q = list(map(int,input().split()))
A = list(map(int,input().split()))
d = {}
out = []
for i in range(len(A)):
    if A[i] not in d:
        d[A[i]] = []
        d[A[i]].append(i+1)
    else:
        d[A[i]].append(i+1)
for _ in range(q):
    x,k = list(map(int,input().split()))
    ans = -1
    if x in d:
        if k <= len(d[x]):
            ans = d[x][k-1]
    out.append(ans)
for _ in out:
    print(_)
