def lastDigit(a,b):
    c = 1
    if a % 10 == 0:
        return 0
    while b > 0:
        if b % 2 != 0:
            c = (c * a) % 10
        b = b // 2
        a = (a**2)%10
    return c

t = int(input())
out = []
for _ in range(t):
    a,b = list(map(int,input().split()))
    out.append(lastDigit(a,b))
for _ in out:
    print(_)