def runGame(a,k):
    a.sort()
    l = 0
    r = len(a) - 1
    e = k
    i = 1
    w = False
    while i <= k:
        if l > r:
            i += 1
            w = False
            continue
        if a[r] <= e:
            r -= 1
            l += 1
            e -= 1
            i += 1
            w = True
        else:
            r -= 1    
    if not w:
        return 'Bob'
    else:
        return 'Alice'

def binarySearch(a,l,r,k):
    if l > r:
        return k
    mid = (l + r) // 2
    result = runGame(a,mid)
    if result == 'Bob':
        return binarySearch(a,l,mid-1,k)
    elif result == 'Alice':
        return binarySearch(a,mid+1,r,mid)

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans.append(binarySearch(a,1,50,0))
for _ in ans:
    print(_)