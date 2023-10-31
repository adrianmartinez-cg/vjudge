#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s, t;
    cin >> s;
    cin >> t;
    int n, m;
    n = s.length();
    m = t.length();
    vector<vector<int>> dp;
    dp.resize(n+1);

    for (int i = 0; i <= n; i++) {
        dp[i].resize(m + 1, 0);
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i-1] != t[j-1]) {
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]); //pega o máximo entre tirar o ultimo c. de s e t
            } else {
                dp[i][j] = 1 + dp[i-1][j-1]; // pode tirar os ultimos dois c. de s e t
            }
        }
    }

    int u,v;
    u = n;
    v = m;
    string commonSubStr = "";
    while(dp[u][v] != 0){
        if (s[u-1] == t[v-1]){
            commonSubStr += s[u-1];
            u--;
            v--;
        }
        else if (dp[u][v-1] > dp[u-1][v]){
            v--;
        }
        else {
            u--;
        }
    }
    for (int i = commonSubStr.length() - 1; i >= 0; i--) {
        cout << commonSubStr[i];
    }

    cout << "\n";
    return 0;   
}