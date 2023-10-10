#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>
using namespace std;
const long long MAX_LENGTH = 1000000000; // equivale a "infinito" 
typedef unordered_map<int, unordered_map<int, int>> AdjacencyMap;
typedef priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> MinPriorityQueue;

vector<int> dijkstra(AdjacencyMap& adj, int n, int origin, MinPriorityQueue& heap) {
    vector<int> distance(n + 1, MAX_LENGTH);
    distance[origin] = 0;
    while (!heap.empty()) {
        int dist = heap.top().first;
        int u = heap.top().second;
        heap.pop();

        if (dist > distance[u]) {
            continue;
        }

        for (auto& kv : adj[u]) {
            int v = kv.first;
            int w = kv.second;
            int oldDist = distance[v];
            int newDist = distance[u] + w;

            if (oldDist > newDist) {
                distance[v] = newDist;
                heap.push({newDist, v});
            }
        }
    }
    return distance;
}

tuple<AdjacencyMap, AdjacencyMap, MinPriorityQueue, MinPriorityQueue> initialize(int n, int origin, int end) {
    AdjacencyMap adj, adjReverse;
    MinPriorityQueue heap, heapReverse;
    long long lengthOrigin;
    long long lengthEnd;

    for (int i = 1; i <= n; i++) {
        adj[i] = {};
        adjReverse[i] = {};
        if(i == origin) {
            lengthOrigin = 0;
        } else {
            lengthOrigin = MAX_LENGTH;
        }
        if(i == end) {
            lengthEnd = 0;
        } else {
            lengthEnd = MAX_LENGTH;
        }
        heap.push({lengthOrigin, i});
        heapReverse.push({lengthEnd, i});
    }
    return { adj, adjReverse, heap, heapReverse };
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int d;
    cin >> d;
    vector<int> paths;
    for (int i = 0; i < d; i++) {
        int n, m, k, s, t;
        cin >> n >> m >> k >> s >> t;
        auto [adj, adjReverse, heap, heapReverse] = initialize(n, s, t);

        for (int j = 0; j < m; j++) {
            int u, v, w;
            cin >> u >> v >> w;
            adj[u][v] = w;
            adjReverse[v][u] = w;
        }
        vector<int> distance = dijkstra(adj, n, s, heap);
        vector<int> distanceReverse = dijkstra(adjReverse, n, t, heapReverse);
        int pathLength = distance[t];
        for (int j = 0; j < k; j++) {
            int u, v, w;
            cin >> u >> v >> w;
            int newDistDirect = distance[u] + w + distanceReverse[v];
            int newDistReverse = distance[v] + w + distanceReverse[u];
            int newDist = min(newDistDirect, newDistReverse);

            if (newDist < pathLength && newDist < MAX_LENGTH) {
                pathLength = newDist;
            }
        }
        paths.push_back(pathLength);
    }
    for (long long i : paths) {
        if(i >= MAX_LENGTH) { i = -1;}
        cout << i << "\n";
    }
    return 0;
}