#include <iostream>
#include <vector>
#include <algorithm>

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

private:
    int V;
    vector<vector<int>> graph;
};

vector<int> parent, componentSize;
int maxSize = 1;

void init(int n) {
    parent.resize(n + 1);
    componentSize.resize(n + 1, 1);
    maxSize = 1;
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
}

int find(int a) {
    if (parent[a] == a) return a;
    return parent[a] = find(parent[a]);
}

void unionSets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        if (componentSize[a] < componentSize[b]) swap(a, b);
        parent[b] = a;
        componentSize[a] += componentSize[b];
        maxSize = max(maxSize, componentSize[a]);
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    Graph g(n);
    vector<pair<int, int>> edges;

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
        g.addEdge(u, v);
    }

    init(n);
    int numComponents = n;
    vector<string> out;

    for (const pair<int, int>& edge : edges) {
        int u = find(edge.first);
        int v = find(edge.second);

        if (u != v) {
            unionSets(u, v);
            numComponents--;
        }
        out.push_back(to_string(numComponents) + " " + to_string(maxSize));
    }

    for (const string& result : out) {
        cout << result << endl;
    }

    return 0;
}