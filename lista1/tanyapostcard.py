def checkMatches(s,t,caseL,L):
    y = 0
    w = 0
    m = len(s)
    left = 0
    right = m - 1
    while left <= right:
        if s[left] in caseL:
            caseL[s[left]] += 1
        else:
            caseL[s[left]] = 1
        if s[left].lower() in L:
            L[s[left].lower()] += 1
        else:
            L[s[left].lower()] = 1
        if left < right:
            if s[right] in caseL:
                caseL[s[right]] += 1
            else:
                caseL[s[right]] = 1
            if s[right].lower() in L:
                L[s[right].lower()] += 1
            else:
                L[s[right].lower()] = 1         
        left += 1
        right -= 1
    for c in t:
        if c in caseL:
            y += 1
            caseL[c] -= 1
        if c.lower() in L:
            w += 1
            L[c.lower()] -= 1
    return y,w

s = input()
t = input()
caseL = {}
L = {}
y,w = checkMatches(s,t,caseL,L)
print(f"{y} {len(s)-y}")