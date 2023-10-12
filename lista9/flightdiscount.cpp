#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;
const ll MAX_LENGTH = 1e18;
typedef priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> MinPriorityQueue;

vector<ll> dijkstra(vector<vector<pair<ll, ll>>>& adj, ll n, ll origin, MinPriorityQueue& heap) {
    vector<ll> distance(n + 1, MAX_LENGTH);
    distance[origin] = 0;
    while (!heap.empty()) {
        ll dist = heap.top().first;
        ll u = heap.top().second;
        heap.pop();

        if (dist > distance[u]) {
            continue;
        }

        for (auto& kv : adj[u]) {
            ll v = kv.first;
            ll w = kv.second;
            ll oldDist = distance[v];
            ll newDist = distance[u] + w;

            if (oldDist > newDist) {
                distance[v] = newDist;
                heap.push({newDist, v});
            }
        }
    }
    return distance;
}

void initialize(ll n , ll origin, MinPriorityQueue& heap){
    for (ll i = 1; i <= n; i++){
        if(i == origin) heap.push({0,i});
        else heap.push({MAX_LENGTH,i});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll n,m;
    cin >> n >> m;
    vector<vector<pair<ll, ll>>> adj(n + 1);
    vector<vector<pair<ll, ll>>> adjReverse(n + 1);
    MinPriorityQueue heap;
    MinPriorityQueue heapReverse;
    initialize(n,1,heap);
    initialize(n,n,heapReverse);
    vector<tuple<ll,ll,ll>> edges;
    for (ll j = 0; j < m; j++){
        ll a,b,c;
        
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        adjReverse[b].push_back({a,c});
        edges.push_back({a,b,c});
    }
    vector<ll> distanceDirect = dijkstra(adj,n,1,heap);
    vector<ll> distanceReverse = dijkstra(adjReverse,n,n,heapReverse);
    ll smallestPrice = MAX_LENGTH;

    for (ll i = 0; i < edges.size(); i++) {
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