import heapq

n,k = list(map(int,input().split()))
A = list(map(int,input().split()))
d = {}
minh = []
pushed = []
c = 0
for i in range(n):
    push = False 
    if A[i] not in d:
        d[A[i]] = True
        heapq.heappush(minh,(i,A[i]))
        c += 1
        push = True
        pushed.append(A[i])       
    elif A[i] in d and not d[A[i]]:
        d[A[i]] = True
        heapq.heappush(minh,(i,A[i]))
        c += 1
        push = True
        pushed.append(A[i])
    if c > k and push:
        first = heapq.heappop(minh)
        d[first[1]] = False
m = len(pushed)
out = ""
if c >= k:
    j = k
else:
    j = c
for i in range(m-1,m-1-j,-1):
    if i < m - 1:
        out += " "
    out += str(pushed[i])
print(j)  
print(out)