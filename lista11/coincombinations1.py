def numCombinations(sum,dp):
    if sum < 0:
        return 0
    for c in C:
        dp[sum] += numCombinations(sum-c,dp)
    return dp[sum]

n,x = map(int,input().split())
p = int(1e9+7)
C = list(map(int,input().split()))
dp = [0 for j in range(x+1)]
dp[0] = 1
print(numCombinations(x,dp))