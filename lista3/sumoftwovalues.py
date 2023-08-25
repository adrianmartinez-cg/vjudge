n,x = list(map(int,input().split()))
aStr = input().split()
A = []
for i in range(len(aStr)):
    A.append((int(aStr[i]),i+1))
A.sort()
l = 0
r = len(A) - 1
out = "IMPOSSIBLE"
while l < r:
    left = A[l][0]
    right = A[r][0]
    if left + right > x:
        r -= 1
    elif left + right < x:
        l += 1
    else:
        if A[l][1] != A[r][1]:
            out = f"{A[l][1]} {A[r][1]}"
        break
print(out)