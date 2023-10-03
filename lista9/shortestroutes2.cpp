#include <iostream>
#include <vector>
#include <climits>
using namespace std;

vector<vector<long long>> floydWarshall(vector<vector<long long>>& adj) {
    int m = adj.size();
    vector<vector<long long>> dist(m, vector<long long>(m, LLONG_MAX));

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < m; j++) {
            if (i == j) {
                dist[i][j] = 0;
            } else if (adj[i][j] != LLONG_MAX) {
                dist[i][j] = adj[i][j];
            }
        }
    }

    for (int k = 1; k < m; k++) {
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < m; j++) {
                if (dist[i][k] != LLONG_MAX && dist[k][j] != LLONG_MAX &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    return dist;
}

int main() {
    int n, m, q;
    cin >> n >> m >> q;

    vector<vector<long long>> adj(n + 1, vector<long long>(n + 1, LLONG_MAX));

    for (int j = 1; j <= n; ++j) {
        adj[j][j] = 0;
    }

    for (int i = 0; i < m; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;

        if (c < adj[a][b]) {
            adj[a][b] = c;
            adj[b][a] = c;
        }
    }

    vector<vector<long long>> distMatrix = floydWarshall(adj);

    vector<long long> dists;

    for (int i = 0; i < q; ++i) {
        int a, b;
        cin >> a >> b;

        if (distMatrix[a][b] == LLONG_MAX) {
            dists.push_back(-1);
        } else {
            dists.push_back(distMatrix[a][b]);
        }
    }

    for (const long long& d : dists) {
        cout << d << endl;
    }

    return 0;
}