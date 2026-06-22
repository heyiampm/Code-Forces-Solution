#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    
   
    vector<int> ones_count(k, 0);
    
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            ones_count[i % k]++;
        }
    }
    
   
    for (int i = 0; i < k; ++i) {
        if (ones_count[i] % 2 != 0) {
            cout << "NO\n";
            return;
        }
    }
    
    cout << "YES\n";
}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}