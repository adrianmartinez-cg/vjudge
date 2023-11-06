def numCombinations(sum,n,dp):
    if sum < 0:
        return 0
    if dp[n][sum] != -1:
        return dp[n][sum]
    if sum == 0: # encontrou combinacao valida
        dp[n][sum] = 1
        return 1
    last = C[n-1]
    dp[n][sum] = numCombinations(sum - last,n,dp) + numCombinations(sum,n-1,dp)
    return dp[n][sum]

n,x = map(int,input().split())
C = list(map(int,input().split()))
dp = [[-1 for j in range(x+1)] for i in range(n+1)]
for j in range(x+1):
    dp[0][j] = 0
print(numCombinations(x,n,dp))
for row in dp:
    print(row)