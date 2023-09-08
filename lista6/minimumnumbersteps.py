s = input()
f = 0
n = 0
p = 1000000007
for i in range(len(s)-1,-1,-1):
    if s[i] == "b":
        f += 1
    elif s[i]== "a":
        n = (n+f) % p
        f = (f*2) % p
print(n) 