#include <iostream>
#include <vector>
#include <deque>

using namespace std;

bool isValidMove(int i, int j, int n, int m, vector<vector<bool>>& visited) {
    return i >= 0 && i < n && j >= 0 && j < m && !visited[i][j];
}

vector<pair<int, int>> getNeighbors(int i, int j, int n, int m, vector<vector<bool>>& visited) {
    vector<pair<int, int>> neighbors;
    pair<int,int> up = {i-1,j};
    pair<int,int> down = {i+1,j};
    pair<int,int> left = {i,j-1};
    pair<int,int> right = {i,j+1};
    int diffrow[] = {-1, 1, 0, 0};
    int diffcol[] = {0, 0, -1, 1};

    for (int k = 0; k < 4; ++k) {
        int ni = i + diffrow[k];
        int nj = j + diffcol[k];
        if (isValidMove(ni, nj, n, m, visited)) {
            neighbors.push_back({ni, nj});
        }
    }

    return neighbors;
}

void dfs(int i, int j, int n, int m, vector<vector<bool>>& visited) {
    deque<pair<int, int>> s;
    s.push_back({i, j});

    while (!s.empty()) {
        pair<int, int> current = s.back();
        s.pop_back();
        int vi = current.first;
        int vj = current.second;
        visited[vi][vj] = true;

        vector<pair<int, int>> neighbors = getNeighbors(vi, vj, n, m, visited);
        for (const pair<int, int>& neighbor : neighbors) {
            int ni = neighbor.first;
            int nj = neighbor.second;
            if (!visited[ni][nj]) {
                s.push_back(neighbor);
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    int numRooms = 0;

    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < m; ++j) {
            if (row[j] == '#') {
                visited[i][j] = true;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!visited[i][j]) {
                numRooms++;
                dfs(i, j, n, m, visited);
            }
        }
    }

    cout << numRooms << endl;

    return 0;
}