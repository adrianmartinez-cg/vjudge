def getStkAndMinTillIndex(s):
    stk = []
    mt = []
    minChar = "{"
    for i in range(len(s)-1,-1,-1):
        stk.append(s[i])
        if s[i] < minChar:
            minChar = s[i]
        mt.append(minChar)
    return stk,mt

s = input()
t = []
u = []
stk,mt = getStkAndMinTillIndex(s)
while len(stk) > 0:
    target = mt[len(mt)-1]
    if len(t) == 0:
        t.append(stk.pop())
    while t[len(t)-1] != target:
        t.append(stk.pop())
    while len(t) > 0:
        u.append(t.pop())
    while mt[len(mt)-1] == target:
        mt.pop()
ans = ""
for c in u:
    ans += c
print(ans)
