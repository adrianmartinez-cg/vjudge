#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int maxLimit = 2e5;
vector<int> parent(maxLimit); // Ancestral do vertice
vector<int> componentSize(maxLimit);   // Tamanho do componente que o vertice esta inserido

void init(int m) {
    for (int i = 0; i < m; i++) {
        parent[i] = i;
        componentSize[i] = 1;
    }
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
        componentSize[a] += componentSize[b];
    }
}

int main() {
    int m, n;
    while (cin >> m && m != 0) {
        init(m);
        vector<pair<int, pair<int, int>>> edges;
        int mstSum = 0;
        int graphSum = 0;

        cin >> n;

        for (int i = 0; i < n; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            edges.push_back({w, {u, v}});
        }

        sort(edges.begin(), edges.end());

        for (const auto& edge : edges) {
            int w = edge.first;
            int u = edge.second.first;
            int v = edge.second.second;
            u = find(u);
            v = find(v);
            graphSum += w;

            if (u != v) {
                mstSum += w;
                unionSets(u, v);
            }
        }

        int maxEconomy = graphSum - mstSum;
        cout << maxEconomy << endl;
    }

    return 0;
}