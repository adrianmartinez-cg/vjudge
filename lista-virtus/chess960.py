def isValid(s):
    bIdx = []
    rIdx = []
    kIdx = -1
    for i in range(len(s)):
        if s[i] == "B":
            bIdx.append(i)
        elif s[i] == "R":
            rIdx.append(i)
        elif s[i] == "K":
            kIdx = i
    bIdx.sort()
    rIdx.sort()
    b1,b2 = bIdx
    r1,r2 = rIdx
    cond1 = b1 % 2 != b2 % 2
    cond2 = kIdx > r1 and kIdx < r2
    if cond1 and cond2:
        return "Yes"
    else:
        return "No"

s = input()
print(isValid(s))