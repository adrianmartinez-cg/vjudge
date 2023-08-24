import heapq

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    f = {}
    h = []
    aStr = input().split()
    for a in aStr:
        if int(a) not in f:
            f[int(a)] = 1
        else:
            f[int(a)] += 1
    for k in f:
        heapq.heappush(h,(-f[k],k))
    np = 0
    a1 = heapq.heappop(h)
    a2 = (0,None)
    if len(h) > 0:
        a2 = heapq.heappop(h)
    while a1[0] < 0 and a2[0] < 0:
        np += 1
        a1 = (a1[0]+1,a1[1])
        a2 = (a2[0]+1,a2[1])
        heapq.heappush(h,a1)
        heapq.heappush(h,a2)
        a1 = heapq.heappop(h)
        a2 = heapq.heappop(h)
    out.append(n - np * 2)
for _ in out:
    print(_)