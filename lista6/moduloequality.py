def getOccurrences(B,n):
    d = {}
    for i in range(n):
        if B[i] not in d:
            d[B[i]] = 1
        else:
            d[B[i]] += 1
    return d

def search(a,num,B,l,r,d):
    if l > r:
        return False
    mid = (l+r)//2
    if B[mid] < num:
        return search(a,num,B,mid+1,r,d)
    elif B[mid] > num:
        return search(a,num,B,l,mid-1,d)
    elif B[mid] == num and d[num] > 0:
        d[num] -= 1
        return True
    
def searchAll(A,B,n,m,x):
    isPermutation = True
    d = getOccurrences(B,n)
    for i in range(n):
        num = (A[i] + x) % m
        if not search(A[i],num,B,0,n-1,d):
            isPermutation = False
            break
    return isPermutation

n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
Amax = min(A)
B = list(map(int,input().split()))
B.sort()
out = 0
lower = m - Amax
for x in range(lower,10**9):
    if searchAll(A,B,n,m,x):
        out = x
        break
print(out%m)