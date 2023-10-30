capacity,n = map(int,input().split())
dp = [[0 for j in range(capacity+1)] for i in range(n)]
W = []
V = []
for _ in range(n):
    w,v = map(int,input().split())
    W.append(w)
    V.append(v)
W0 = W[0]
V0 = V[0]
for j in range(W0,capacity+1): #preenchendo primeira linha
    dp[0][j] = V[0]
for i in range(1,n):
    for j in range(1,capacity+1):
        if W[i] > j:
            dp[i][j] = dp[i-1][j] # o item nao cabe, pega sol. anterior
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j - W[i]] + V[i])
print(dp[n-1][capacity])