def closestToCenter(A,l,r,c,mid):
    if l > r:
        return c
    m = (l + r) // 2
    elem = A[m]
    if abs(elem-mid) < abs(c-mid):
        closest = elem
    else:
        closest = c
    if elem < mid:
        return closestToCenter(A,m+1,r,closest,mid)
    elif elem > mid:
        return closestToCenter(A,l,m-1,closest,mid)
    else:
        return elem

def calcMaxDist(A,l,r,c):
    return max(abs(c-A[l]),abs(c-A[r]))

n,k = list(map(int,input().split()))
roomStr = input()
X = []
for i in range(n):
    if roomStr[i] == "0":
        X.append(i)
l = 0
r = k
distCow = 10**5
while r <= len(X) - 1:
    mid = (X[l] + X[r])/2
    closest = closestToCenter(X,l,r,X[r],mid)
    maxDist = calcMaxDist(X,l,r,closest)
    if maxDist < distCow: distCow = maxDist
    l += 1
    r += 1
print(distCow)