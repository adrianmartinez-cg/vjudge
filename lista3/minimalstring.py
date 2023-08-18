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
n = len(stk)

while n > 0:
    target = mt[n-1]
    if len(t) == 0:
        t.append(stk.pop())
        n -= 1
    while t[len(t)-1] > target:
        t.append(stk.pop())
        n -= 1
    u.append(t.pop())

while len(t) > 0:
    u.append(t.pop())
ans = ""
for c in u:
    ans += c
print(ans)