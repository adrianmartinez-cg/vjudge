import heapq

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    S = list(map(int,input().split()))
    maxh = []
    power = 0
    for i in range(len(S)):
        if S[i] > 0:
            heapq.heappush(maxh,-S[i])
        if S[i] == 0:
            if len(maxh) > 0:
                power += abs(heapq.heappop(maxh))
    out.append(power)
for _ in out:
    print(_)