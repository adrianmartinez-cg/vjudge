n,m = list(map(int,input().split()))
d = {}
p = int(1e9+7)
numStrings = 1
for i in range(n):
    s = list(input())
    for j in range(len(s)):
        if j not in d:
            d[j] = set()
        d[j].add(s[j])
for i in range(m):
    numStrings = (numStrings * len(d[i])) % p
print(numStrings)