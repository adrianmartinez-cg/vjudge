#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

vector<int> parent,componentSize;
map<pair<int, int>, int> edgesId;
map<int, int> parentNode;
map<int, map<int, int>> adj;

vector<int> init(int n) {
    parent.resize(n + 1);
    componentSize.resize(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    return parent;
}

int find(int a) {
    if (parent[a] == a)
        return a;
    parent[a] = find(parent[a]);
    return parent[a];
}

void unionSets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        if (componentSize[a] < componentSize[b])
            swap(a, b);
        parent[b] = a;
    }
    componentSize[a] += componentSize[b];
}

int startVertex = 0;
bool foundCycle = false;
vector<bool> visited;
vector<int> traversal;

void dfs(int i, int p) {
    visited[i] = true;
    traversal.push_back(i);
    for (const auto& c : adj[i]) {
        if (visited[c.first] && c.first != p) {
            traversal.push_back(c.first);
            startVertex = c.first;
            foundCycle = true;
            return;
        }
        if (c.first != p && !visited[c.first])
            dfs(c.first, i);
    }
    if (!foundCycle)
        traversal.pop_back();
}

string getCycle(int c) {
    vector<int> cycle;
    vector<int> cycleEdges;
    bool cycleStart = false;
    for (int i : traversal) {
        if (i == c && cycleStart) {
            cycle.push_back(i);
            break;
        }
        if (i == c)
            cycleStart = true;
        if (cycleStart)
            cycle.push_back(i);
    }
    for (int i = 0; i < cycle.size() - 1; i++) {
        pair<int, int> edge = {cycle[i], cycle[i + 1]};
        cycleEdges.push_back(edgesId[edge]);
    }
    sort(cycleEdges.begin(), cycleEdges.end());
    string out = "";
    for (int i = 0; i < cycleEdges.size(); i++) {
        out += to_string(cycleEdges[i]);
        if (i < cycleEdges.size() - 1)
            out += " ";
    }
    return out;
}

int main() {
    int t;
    cin >> t;
    vector<string> cycles;

    for (int j = 0; j < t; j++) {
        int n, m;
        cin >> n >> m;
        parent = init(n);
        string cycle = "-1";
        foundCycle = false;
        visited.assign(n + 1, false);
        traversal.clear();
        startVertex = 0;
        edgesId.clear();
        parentNode.clear();
        adj.clear();

        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            edgesId[{u, v}] = i + 1;
            edgesId[{v, u}] = i + 1;
            adj[u][v] = 1;
            adj[v][u] = 1;
            parentNode[v] = u;
            int pu = find(u), pv = find(v);

            if (pu != pv)
                unionSets(u, v);
            else {
                if (!foundCycle) {
                    dfs(v, u);
                    cycle = getCycle(startVertex);
                }
            }
        }
        cycles.push_back(cycle);
    }

    for (const string& c : cycles)
        cout << c << endl;

    return 0;
}