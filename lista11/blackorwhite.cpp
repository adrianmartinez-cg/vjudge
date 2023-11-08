#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
const int maxVal = 1000001;

int solve(int i , int lastWhite , int lastBlack, vector<int>& seq, vector<vector<vector<int>>>& dp){
    int n = dp.size();
    int ans;

    if(i == n) return 0;

    if(dp[i][lastWhite][lastBlack] != -1) return dp[i][lastWhite][lastBlack];

    ans = 1 + solve(i+1,lastWhite,lastBlack,seq,dp);
    if(seq[lastWhite] > seq[i]) ans = min(ans,solve(i+1,i,lastBlack,seq,dp));
    if(seq[lastBlack] < seq[i]) ans = min(ans,solve(i+1,lastWhite,i,seq,dp));

    dp[i][lastWhite][lastBlack] = ans;
    return dp[i][lastWhite][lastBlack];
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> out;

    int n;
    cin >> n;
    while (n >= 1){
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n+2, vector<int>(n+2, -1)));
        vector<int> seq(n);
        for (int i = 0; i < n; i++) {
            cin >> seq[i];
        }
        seq.push_back(-maxVal);
        seq.push_back(maxVal);
        out.push_back(solve(0, n + 1, n, seq, dp)); // lastWhite tem que ser garantidamente o maior, e lastBlack o menor
        cin >> n;    
    }

    for (int j = 0; j < out.size(); j++){
        cout << out[j] << "\n";
    }

    return 0;
}
