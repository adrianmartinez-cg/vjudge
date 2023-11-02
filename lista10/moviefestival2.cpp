#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    cin >> n >> k;
    vector<tuple<int,int,int>> movies;
    for(int i = 0; i < n; i++){
        int a,b;
        cin >> a >> b;
        movies.push_back({b,a,i});
    }
    sort(movies.begin(), movies.end(), [](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
        return get<0>(a) > get<0>(b); 
    });

    set<pair<int,int>> busy;
    int cantWatch = 0;
    while(!movies.empty()){
        tuple<int,int,int> movie = movies.back();
        pair<int,int> movie_ = {-get<0>(movie),get<2>(movie)};
        pair<int,int> movieStartTime = {-get<1>(movie),-1};
        auto it = busy.lower_bound(movieStartTime);
        if(it != busy.end()){
            pair<int,int> closestMovie = *it;
            busy.erase(closestMovie);
            busy.insert(movie_);
        } else {
            if(busy.size() < k){
                busy.insert(movie_);
            } else {
                cantWatch++;
            }
        }
        movies.pop_back();
    }
    cout << n - cantWatch << "\n";

    return 0;   
}