t = int(input())
out = []
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    x = 10**(a - 1)
    y = 10**(b - 1)
    if x >= y:
        x += 10**(c-1)
    else:
        y += 10**(c-1)
    ans = f"{x} {y}"
    out.append(ans)
for _ in out:
    print(_)