#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int capacity, n;
    cin >> capacity >> n;
    vector<vector<int>> dp;
    dp.resize(n);
    for (int i = 0; i < n; i++) {
        dp[i].resize(capacity + 1, 0);
    }

    vector<int> W(n);
    vector<int> V(n);

    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;
        W[i] = w;
        V[i] = v;
    }

    int W0 = W[0];
    int V0 = V[0];

    for (int j = W0; j <= capacity; j++) { // preenchendo primeira linha
        dp[0][j] = V0;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= capacity; j++) {
            if (W[i] > j) {
                dp[i][j] = dp[i - 1][j]; // item nao cabe
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]); // maximo entre não escolher iesimo item e escolher iesimo item
            }
        }
    }

    cout << dp[n - 1][capacity] << "\n";

    return 0;
}