#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

class Graph {
private:
    unordered_map<int, vector<int>> graph;
    int V;
    int maxDist;
    int lastVisited;

public:
    Graph(int vertices) : V(vertices), maxDist(-1), lastVisited(-1) {}

    void addEdge(int u, int v) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    void DFSUtil(int v, set<int>& visited, vector<int>& traversal, int distance) {
        if (distance > maxDist) {
            maxDist = distance;
            lastVisited = v;
        }
        visited.insert(v);
        traversal.push_back(v);

        for (int neighbour : graph[v]) {
            if (visited.find(neighbour) == visited.end()) {
                DFSUtil(neighbour, visited, traversal, distance + 1);
            }
        }
    }

    vector<int> DFS(int v) {
        set<int> visited;
        vector<int> traversal;
        DFSUtil(v, visited, traversal, 0);
        return traversal;
    }

    int findDiameter() {
        maxDist = -1;
        DFS(lastVisited);
        return maxDist;
    }
};

int main() {
    int n;
    cin >> n;

    Graph g(n);
    int lastV = -1;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u - 1, v - 1);
        lastV = u - 1;
    }

    g.DFS(lastV);
    int dist1 = g.findDiameter();

    cout << dist1 << endl;

    return 0;
}