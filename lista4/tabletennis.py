n,k = list(map(int,input().split()))
A = list(map(int,input().split()))
s = max(A)
nw = 0
l = 0
r = 1
out = s
while nw < k:
    left,right = A[l],A[r]
    if left == s:
        break
    else:
        if left > right:
            A.append(right)
            nw += 1
            if nw == k: 
                out = left
            l += 1
            r += 1
            A[l] = left
        else:
            A.append(left)
            nw = 1
            if nw == k: 
                out = right
            l += 1
            r += 1
print(out)