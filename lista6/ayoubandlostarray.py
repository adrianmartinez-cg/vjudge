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
    return d
