#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

struct Edge {
    int to, weight;
    Edge(int _to, int _weight) : to(_to), weight(_weight) {}
};

vector<int> djikstra(const vector<vector<Edge>>& adj, int origin, int destination) {
    int n = adj.size();
    vector<int> distance(n, numeric_limits<int>::max());
    distance[origin] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, origin});

    while (!pq.empty()) {
        int dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (dist > distance[u]) {
            continue;
        }

        for (const Edge& edge : adj[u]) {
            int v = edge.to;
            int newDist = distance[u] + edge.weight;
            if (newDist < distance[v]) {
                distance[v] = newDist;
                pq.push({newDist, v});
            }
        }
    }

    return distance;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    cin >> n >> m >> q;

    vector<vector<Edge>> adj(n + 1);

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].emplace_back(b, c);
        adj[b].emplace_back(a, c);
    }

    vector<int> dist;

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        vector<int> distance = djikstra(adj, a, b);
        int d = distance[b];
        if (d == numeric_limits<int>::max()) {
            dist.push_back(-1);
        } else {
            dist.push_back(d);
        }
    }

    for (int d : dist) {
        cout << d << endl;
    }

    return 0;
}