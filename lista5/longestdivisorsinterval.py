import math

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    i = 1
    while n % i == 0:
        i += 1
    out.append(i-1)
for _ in out:
    print(_)