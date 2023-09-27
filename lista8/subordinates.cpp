#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

class Graph {
public:
    Graph(int vertices) : V(vertices) {}

    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    void DFSUtil(int v, set<int>& visited) {
        visited.insert(v);
        for (int neighbour : graph[v]) {
            if (visited.find(neighbour) == visited.end()) {
                DFSUtil(neighbour, visited);
            }
        }
    }

    int DFS(int v) {
        set<int> visited;
        DFSUtil(v, visited);
        return visited.size() - 1;
    }

private:
    unordered_map<int, vector<int>> graph;
    int V;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> A(n);

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    Graph g(n);

    for (int i = 0; i < n; i++) {
        g.addEdge(A[i], i + 2);
    }

    string out = "";
    for (int i = 1; i <= n; i++) {
        int count = g.DFS(i);
        out += to_string(count);
        if (i < n) out += " ";
    }

    cout << out << endl;

    return 0;
}