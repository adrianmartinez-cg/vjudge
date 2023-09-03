def fastPow(a,b):
    if b % 2 == 0:
        if b == 2 or b == 0:
            return a ** b
        else:
            return fastPow(a*a,b//2)
    else:
        return a * fastPow(a,b-1)

n = int(input())
m = int(input())
if n <= 27: # m < 2 ** 27
    print(m % fastPow(2,n))
else:
    print(m)