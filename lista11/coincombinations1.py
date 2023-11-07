import sys

def numCombinations(sum,dp):
    if sum < 0:
        return 0
    if dp[sum] != -1:
        return dp[sum]
    dp[sum] = 0
    for c in C:
        dp[sum] = (dp[sum] + numCombinations(sum-c,dp))%p
    return dp[sum]

sys.setrecursionlimit(int(1e9))
n,x = map(int,input().split())
p = int(1e9+7)
C = list(map(int,input().split()))
dp = [-1 for j in range(x+1)]
dp[0] = 1
print(numCombinations(x,dp))