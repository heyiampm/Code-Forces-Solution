#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    
    map<int, int> counts;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        counts[a]++;
    }
    
    vector<pair<int, int>> elements(counts.begin(), counts.end());
    int m = elements.size();
    
    vector<bool> next_win(m, false);
    vector<bool> is_L(m, false);
    
    int r = m - 1;
    int L_count_in_window = 0;
    
    for (int i = m - 1; i >= 0; --i) {
        while (elements[r].first > elements[i].first + k) {
            if (is_L[r]) {
                L_count_in_window--;
            }
            r--;
        }
        
        if (L_count_in_window > 0) {
            next_win[i] = true;
        } else {
            next_win[i] = false;
        }
        
        if (!next_win[i] && (elements[i].second % 2 != 0)) {
            is_L[i] = true;
        } else {
            is_L[i] = false;
        }
        
        if (is_L[i]) {
            L_count_in_window++;
        }
    }
    
    bool arseniy_can_win = false;
    for (int i = 0; i < m; ++i) {
        if (next_win[i] || (elements[i].second % 2 == 0)) {
            arseniy_can_win = true;
            break;
        }
    }
    
    if (arseniy_can_win) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
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