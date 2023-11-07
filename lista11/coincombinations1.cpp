#include <iostream>
#include <vector>
using namespace std;
const long long p = 1000000007;

long long numCombinations(long long sum, vector<long long>& dp, vector<int>& C){
    if(sum < 0){
        return 0;
    }
    if(dp[sum] != -1){
        return dp[sum];
    }
    dp[sum] = 0;
    for (int c : C){
        dp[sum] = (dp[sum] + numCombinations(sum-c,dp,C))%p;
    }
    return dp[sum];
    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,x;
    cin >> n >> x;
    vector<long long> dp(x+1,-1);
    dp[0] = 1;
    vector<int> C(n);
    for (int i = 0; i < n; i++){
        cin >> C[i];
    }
    cout << numCombinations(x,dp,C) << "\n";
    
}