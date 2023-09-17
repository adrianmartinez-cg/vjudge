s = input()
numSeqBefore = 0
count = 0
p = int(1e9+7)
for i in range(len(s)):
    if s[i] == 'a':
        count = (count + (numSeqBefore + 1)) % p
    elif s[i] == 'b':
        numSeqBefore = count
print(count)