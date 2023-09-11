def calcMod3Interval(l,r):
    d = {0:0,1:0,2:0}
    qtElements = r-l+ 1
    q = qtElements // 3
    rm = qtElements % 3
    rmLeft = l % 3
    # pegando os elementos dentro de cada "trio" completo
    d[rmLeft] = q
    d[(rmLeft+1)%3] = q
    d[(rmLeft+2)%3] = q
    # pegando os elementos restantes
    for i in range(r-rm+1,r+1):
        d[i%3] += 1
    return d[0],d[1],d[2]

n,l,r = list(map(int,input().split()))
qt0,qt1,qt2 = calcMod3Interval(l,r)
qtMod0,qtMod1,qtMod2 = 1,0,0
p = int(1e9+7)
for i in range(1,n+1):
    nextMod0 = (qtMod0 * qt0 + qtMod1 * qt2 + qtMod2 * qt1)%p
    nextMod1 = (qtMod0 * qt1 + qtMod1 * qt0 + qtMod2 * qt2)%p
    nextMod2 = (qtMod0 * qt2 + qtMod1 * qt1 + qtMod2 * qt0)%p
    qtMod0,qtMod1,qtMod2 = nextMod0,nextMod1,nextMod2
print(qtMod0)