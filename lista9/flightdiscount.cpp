#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;
const ll MAX_LENGTH = 2e14+1; // soma maxima das arestas é 2e14
typedef priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> MinPriorityQueue;

vector<ll> dijkstra(vector<vector<pair<int, int>>>& adj, int n, int origin, MinPriorityQueue& heap) {
    vector<ll> distance(n + 1, MAX_LENGTH);
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

void initialize(int n , int origin, MinPriorityQueue& heap){
    for (int i = 1; i <= n; i++){
        if(i == origin) heap.push({0,i});
        else heap.push({MAX_LENGTH,i});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);
    MinPriorityQueue heap;
    MinPriorityQueue heapReverse;
    initialize(n,1,heap);
    initialize(n,n,heapReverse);
    vector<tuple<int,int,int>> edges;
    for (int j = 0; j < m; j++){
        int a,b,c;
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        edges.push_back({a,b,c});
    }
    vector<ll> distanceDirect = dijkstra(adj,n,1,heap);
    vector<ll> distanceReverse = dijkstra(adj,n,n,heapReverse);
    ll smallestPrice = MAX_LENGTH;

    for (int i = 0; i < edges.size(); i++) {
        auto [a,b,c] = edges[i];
        ll distToA = distanceDirect[a];
        ll distToB = distanceReverse[b];
        ll priceWithDiscount = c / 2;
        ll totalPrice  = distToA + distToB + priceWithDiscount;
        if(totalPrice < smallestPrice){
            smallestPrice = totalPrice;
        }
    }
    cout << smallestPrice << "\n";
    return 0;
}