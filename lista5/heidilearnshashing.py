import math

r = int(input())
intRoot = math.isqrt(r)
s = r - 1
ans = "NO"
for x in range(1,intRoot+1):
    if s % x == 0:
        floatY = (s//x - x - 1) / 2
        intY = (s//x - x - 1) // 2
        if intY > 0 and floatY == intY: # checando se a expressao dá um inteiro
            ans = f"{x} {intY}"
            break
print(ans)