n = int(input())
d = list(map(int,input().split()))
l = 0
r = len(d) - 1
se = 0
sd = 0
s = 0
checkL , checkR = True,True
while l < r:
    if checkL: 
        se += d[l]
        checkL = False
    if checkR:
        sd += d[r]
        checkR = False
    if se < sd:
        l += 1
        checkL = True
    elif se == sd:
        s = se
        l += 1
        checkL = True
    else:
        r -= 1
        checkR = True
print(s)