import heapq

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    S = list(map(int,input().split()))
    maxh = []
    minh = []
    power = 0
    for i in range(len(S)):
        heapq.heappush(minh,(S[i],i))
        heapq.heappush(maxh,(-S[i],i))
    bonus = heapq.heappop(maxh)
    hero = heapq.heappop(minh)
    while hero[0] == 0:
        if hero[1] > bonus[1]:
            power += abs(bonus[0])
        bonus = heapq.heappop(maxh)
        hero = heapq.heappop(minh)
    out.append(power)
for _ in out:
    print(_)