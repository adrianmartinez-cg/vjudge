#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
typedef long long ll;

bool cmpSort(const tuple<ll, ll,ll>& a, const tuple<ll,ll,ll>& b){
    return get<0>(a) < get<0>(b);
}

ll solve(int i , vector<ll>& dp, vector<tuple<ll,ll,ll>>& P){
    int n = dp.size();
    if(i >= n){
        return 0;
    }
    if(dp[i] != -1){
        return dp[i];
    }
    dp[i] = 0;
    tuple<ll,ll,ll> p = P[i];
    ll end = get<1>(p);
    ll v = get<2>(p);
    auto it = upper_bound(P.begin(),P.end(),make_tuple(end,end,end));
    int next = it - P.begin();
    ll ans = max(solve(i+1,dp,P), v + solve(next,dp,P));
    dp[i] = ans;
    return dp[i];
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<tuple<ll,ll,ll>> P(n);
    vector<ll> dp(n,-1);
    for (int i = 0; i < n; i++){
        ll a,b,p;
        cin >> a >> b >> p;
        P[i] = {a,b,p};
    }
    sort(P.begin(),P.end(),cmpSort);
    solve(0,dp,P);
    cout << dp[n-1] << "\n";
 
    return 0;
}