#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Graph {
public:
    Graph(int vertices) : V(vertices) {}

    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    vector<int> getNeighbors(int u) {
        return graph[u];
    }

    void topologicalSortUtil(int v, vector<bool>& visited, vector<int>& stack) {
        visited[v] = true;
        for (int neighbor : graph[v]) {
            if (!visited[neighbor]) {
                topologicalSortUtil(neighbor, visited, stack);
            }
        }
        stack.push_back(v);
    }

    vector<int> topologicalSort() {
        vector<bool> visited(V, false);
        vector<int> stack;
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                topologicalSortUtil(i, visited, stack);
            }
        }
        return stack;
    }

private:
    map<int, vector<int>> graph;
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
    vector<int> numSubs(n, 0);

    for (int i = 0; i < n; i++) {
        g.addEdge(A[i] - 1, i + 1);
    }

    vector<int> topOrder = g.topologicalSort();
    for (int k : topOrder) {
        vector<int> neighbors = g.getNeighbors(k);
        for (int m : neighbors) {
            numSubs[k] += 1 + numSubs[m];
        }
    }

    for (int i = 0; i < n; i++) {
        cout << numSubs[i];
        if (i < n) {
            cout << " ";
        }
    }
    cout << endl;
    return 0;
}