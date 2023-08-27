import heapq

n = int(input())
s = input()
maxh = []
minh = []
r = list("0000000000")
for i in range(len(r)):
    heapq.heappush(minh,i)
    heapq.heappush(maxh,-i)
for c in s:
    if c == "L":
        while len(minh) > 0:
            room = heapq.heappop(minh)
            if r[room] == "0": 
                r[room] = "1"
                break
    elif c == "R":
        while len(maxh) > 0:
            room = abs(heapq.heappop(maxh))
            if r[room] == "0": 
                r[room] = "1"
                break
    else:
        room = int(c)
        r[room] = "0"
        heapq.heappush(minh,room)
        heapq.heappush(maxh,-room)
out = ""
for c in r:
    out += c
print(out)