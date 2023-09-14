t = int(input())
out = []
for _ in range(t):
    n,k = list(map(int,input().split()))
    s = list("a"*n)
    i = n - 2
    while i >= 0:
        numRepsPattern = n - (i + 1)
        k -= numRepsPattern
        if k <= 0:
            leftBPos = i
            rightBPos = (i + 1) - k
            s[leftBPos] = "b"
            s[rightBPos] = "b"
            break
        else:
            i -= 1
    out.append("".join(s))
for _ in out:
    print(_)