#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

bool solve(vector<int>& A, long long k, vector<int>& numbers) {
    long long sum;
    bool lessThanK;
    do {
        lessThanK = true;
        sum = 0;
        for(int i=0; i < 10; i++){
            sum += numbers[i] * A[i];
            if(sum > k) {
                lessThanK = false;
                break;
            }
        }
        if(lessThanK) break;
    } while (next_permutation(numbers.begin(), numbers.end()));
    return lessThanK;
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    vector<vector<int>> ans;
    for (int _ = 0; _ < t; _++){
        vector<int> A(10);
        for(int j = 0; j < 10; j++){
            cin >> A[j];
        }

        long long k;
        cin >> k;
        vector<int> numbers = {0,1,2,3,4,5,6,7,8,9};
        if(solve(A,k,numbers)){
            ans.push_back(numbers);
        } else {
            ans.push_back({-1});
        }
    }
    
    for (const vector<int>& row : ans) {
        for (int value : row){
            cout << value << " ";
        }
        cout << "\n";
    }
   
    return 0;   
}