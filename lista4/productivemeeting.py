import heapq

def getTalks(h,out):
    n = 0
    mt = []
    a1 = heapq.heappop(h)
    a2 = heapq.heappop(h)
    while a1[0] < 0 and a2[0] < 0:
        n += 1
        a1 = (a1[0]+1,a1[1])
        a2 = (a2[0]+1,a2[1])
        mt.append((a1[1],a2[1]))
        heapq.heappush(h,a1)
        heapq.heappush(h,a2)
        a1 = heapq.heappop(h)
        a2 = heapq.heappop(h)
    out.append(n)
    for m in mt:
        out.append(f"{m[0]} {m[1]}")
    
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    aStr = input().split()
    h = []
    heapq.heapify(h)
    for i in range(len(aStr)):
        heapq.heappush(h,(-int(aStr[i]),i+1))
    getTalks(h,out)
for _ in out:
    print(_)
