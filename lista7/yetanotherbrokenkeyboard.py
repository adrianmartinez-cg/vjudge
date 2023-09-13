n,k = list(map(int,input().split()))
st = list(input())
ls = input().split()
keys = set()
numSubStr = 0
for ch in ls:
    keys.add(ch)
lastLetter = -1
subStrLen = 0
for i in range(len(st)):
    if (st[i] not in keys) or (i == n - 1):
        subStrLen = i - (lastLetter+1)
        if (i == n - 1) and (st[i] in keys): subStrLen += 1
        numSubStr += subStrLen * (subStrLen + 1) // 2
        lastLetter = i 
print(numSubStr)