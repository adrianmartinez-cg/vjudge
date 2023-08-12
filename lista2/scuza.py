def accumulativeSum(h,n):
    acc = [h[0]]
    for i in range(1,n):
        acc.append(h[i] + acc[i-1])
    return acc

def maxHeight(h,n):
    mh = []
    hmax = h[0]
    for s in h:
        if s > hmax:
            hmax = s
        mh.append(hmax)
    return mh

def returnAccSumAndMaxHeight(h,n):
    acc = [h[0]]
    mh = [h[0]]
    hmax = h[0]
    for i in range(1,n):
        acc.append(h[i] + acc[i-1])
        if h[i] > hmax:
            hmax = h[i]
        mh.append(hmax)
    return acc,mh

def binarySearch(h,l,r,k,j):
    if l > r:
        return j
    mid = (l+r)//2
    if h[mid] > k:
        return binarySearch(h,l,mid-1,k,j)
    else:
        return binarySearch(h,mid+1,r,k,mid)

t = int(input())
ans = []
for _ in range(t):
    n,q = list(map(int,input().split()))
    h = list(map(int,input().split()))
    K = list(map(int,input().split()))
    th,mh = returnAccSumAndMaxHeight(h,n)
    x = ""
    for i in range(q):
        pos = binarySearch(mh,0,n-1,K[i],-1)
        if i > 0:
            x += " "
        if pos == -1:
            x += "0"
        else:
            x += str(th[pos])
    ans.append(x)
for _ in ans:
    print(_)