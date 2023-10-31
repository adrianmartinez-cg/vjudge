s = list(input())
t = list(input())
n = len(s)
m = len(t) 
dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] != t[j-1]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #pega o máximo entre tirar o ultimo c. de s e t
        else:
            dp[i][j] = 1 + dp[i-1][j-1] #pode tirar os ultimos dois c. de s e t

i,j = n,m
commonSubStr = ""
while dp[i][j] != 0:
    if s[i-1] == t[j-1]:
        commonSubStr += s[i-1]
        i -= 1 
        j -= 1
        continue
    if dp[i][j-1] > dp[i-1][j]:
        j -= 1
        continue
    i -= 1
    continue
print(commonSubStr[::-1])