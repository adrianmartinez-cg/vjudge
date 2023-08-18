def splitTwoAndCheck(s,d):
    isConcat = "0"
    for i in range(1, len(s)):
        s1 = s[:i]
        s2 = s[i:]
        if s1 in d and s2 in d:
            isConcat = "1"
            break
    return isConcat

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    d = {}
    x = ""
    S = []
    for k in range(n):
        s = input()
        d[s] = 1
        S.append(s)
    for s in S:
        x += splitTwoAndCheck(s,d)
    ans.append(x)
for _ in ans:
    print(_)