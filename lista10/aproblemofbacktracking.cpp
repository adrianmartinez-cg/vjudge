#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

string solve(vector<int>& A, long long k, vector<int>& numbers) {
    // primeiro caso
    long long sum = 0;
    bool lessThanK = true;
    string ans = "";
    for(int i=0; i < 10; i++){
        sum += numbers[i] * A[i];
        if(sum > k) {
            lessThanK = false;
            break;
        }
        ans += to_string(numbers[i]);
        if(i < 9) ans += " ";
    }
    if(lessThanK) return ans;
    else{
        // gerando permutacoes em ordem lexicografica
        while(next_permutation(numbers.begin(),numbers.end())){
            sum = 0;
            lessThanK = true;
            ans = "";
            for(int i=0; i < 10; i++){
                sum += numbers[i] * A[i];
                if(sum > k) {
                    lessThanK = false;
                    break;
                }
                ans += to_string(numbers[i]);
                if(i < 9) ans += " ";
            }
            if(lessThanK) break;
        }
    }
    if(!lessThanK) return "-1";
    return ans;
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    vector<string> ans;
    for (int _ = 0; _ < t; _++){
        vector<int> A(10);
        for(int j = 0; j < 10; j++){
            cin >> A[j];
        }

        long long k;
        cin >> k;
        vector<int> numbers = {0,1,2,3,4,5,6,7,8,9};
        ans.push_back(solve(A,k,numbers));
    }
    
      for (int i = 0; i < t; i++) {
        cout << ans[i] << "\n";
    }
   
    return 0;   
}