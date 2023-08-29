import math

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    ans = f"1 {n-1}"
    if n % 2 == 0:
        b = n // 2
        ans = f"{b} {b}"
    else:
        for i in range(2,math.isqrt(n)+1):
            if n % i == 0:
                b = n // i
                ans = f"{b} {n-b}"
                break
    out.append(ans)
for _ in out:
    print(_)