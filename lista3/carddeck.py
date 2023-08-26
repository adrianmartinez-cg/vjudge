t = int(input())
out = []
for _ in range(t):
    n = int(input())
    p = input().split()
    d = {}
    deck = ""
    for i in range(n-1,-1,-1):
        p[i] = int(p[i])
        d[p[i]] = (i,False)
    ps = sorted(p,reverse=True)
    j = 0
    m = 0
    target = ps[j]
    r = n - 1
    while m < n:
        l = d[target][0]
        for i in range(l,r+1):
            if m > 0: deck += " "
            deck += str(p[i])
            d[p[i]] = (i,True)
            m += 1
        r = l - 1
        while d[ps[j]][1] == True:
            j += 1
            if j > n - 1: break
        if j > n - 1: break
        target = ps[j]
    out.append(deck)
for _ in out:
    print(_)