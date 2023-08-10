n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
for i in range(n):
    c.append(a[i]-b[i])
c.sort()
l = 0
r = n - 1
p = 0
while l < r:
    if c[r] + c[l] > 0:
        p += r - l
        r -= 1
    else:
        l += 1
print(p)