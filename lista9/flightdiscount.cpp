#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
const long long MAX_LENGTH = 1000000000; // equivale a "infinito" 
typedef priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> MinPriorityQueue;

int dijkstra(vector<vector<pair<int, int>>>& adj, int n, int origin, MinPriorityQueue& heap, map<int,int>& pred) {
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
                pred[v] = u;
            }
        }
    }
    return distance[n];
}

void initialize(int n , MinPriorityQueue& heap, map<int,int>& pred){
    for (int i = 1; i <= n; i++){
        pred[i] = 0;
        if(i == 1) heap.push({0,i});
        else heap.push({MAX_LENGTH,i});
    }
}

vector<int> findPath(int n , map<int,int>& pred){
    vector<int> path;
    int i = n;

    while (i != 1) {
        path.push_back(pred[i]);
        i = pred[i];
    }

    reverse(path.begin(), path.end());
    path.push_back(n);

    return path;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);;
    map<int,int> pred;
    MinPriorityQueue heap;
    initialize(n,heap,pred);
    map<pair<int,int>,int> edgesWeight;
    for (int j = 0; j < m; j++){
        int a,b,c;
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        edgesWeight[{a,b}] = c;
    }
    int normalRoute = dijkstra(adj,n,1,heap,pred);
    vector<int> shortestPath = findPath(n,pred);
    int edgeMaxWeight = 0;

    for (int i = 0; i < shortestPath.size() - 1; i++) {
        pair<int, int> edge = {shortestPath[i], shortestPath[i + 1]};
        int w = edgesWeight[edge];

        if (w > edgeMaxWeight) {
            edgeMaxWeight = w;
        }
    }

    int discountRoute = normalRoute - edgeMaxWeight + (edgeMaxWeight / 2);
    cout << discountRoute << "\n";

    return 0;
}