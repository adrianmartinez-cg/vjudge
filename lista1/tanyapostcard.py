s = input()
t = input()
chrs = list(s)
L = {}
y = 0
w = 0
for c in t:
    if c in L:
        L[c] += 1
    else:
        L[c] = 1
for i in range(len(s)):
    if s[i] in L:
        if L[s[i]] > 0:
            y += 1
            L[s[i]] -= 1
            chrs[i] = "*"
for i in range(len(s)):
    if chrs[i] != "*":
        if s[i].swapcase() in L:
            if L[s[i].swapcase()] > 0:
                L[s[i].swapcase()] -= 1
                w += 1
print(f"{y} {w}")