#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Graph {
public:
    Graph(int vertices) : V(vertices) {
        graph.resize(vertices + 1);
    }

    void addEdge(int u, int v) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> dfs(int u, vector<bool>& visited) {
        deque<int> s;
        vector<int> component;
        s.push_back(u);
        while (!s.empty()) {
            int v = s.back();
            s.pop_back();
            component.push_back(v);
            visited[v] = true;
            for (int neighbor : graph[v]) {
                if (!visited[neighbor]) {
                    s.push_back(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        return component;
    }

    pair<int, int> connectedComponents() {
        vector<bool> visited(V + 1, false);
        vector<vector<int>> components;
        int maxSize = 0;
        for (int vertex = 1; vertex <= V; vertex++) {
            if (!visited[vertex]) {
                vector<int> component = dfs(vertex, visited);
                components.push_back(component);
                if (component.size() > maxSize) {
                    maxSize = static_cast<int>(component.size());
                }
            }
        }
        return {static_cast<int>(components.size()), maxSize};
    }

private:
    int V;
    vector<vector<int>> graph;
};

int main() {
    int n, m;
    cin >> n >> m;
    Graph g(n);
    vector<string> out;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
        auto [components, maxSize] = g.connectedComponents();
        out.push_back(to_string(components) + " " + to_string(maxSize));
    }
    for (const string& result : out) {
        cout << result << endl;
    }
    return 0;
}