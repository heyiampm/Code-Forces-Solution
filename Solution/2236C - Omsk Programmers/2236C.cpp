#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    long long a, b, x;
    cin >> a >> b >> x;

  
    vector<pair<long long, int>> states_a;
    long long curr_a = a;
    int steps_a = 0;
    states_a.push_back({curr_a, steps_a});
    while (curr_a > 0) {
        curr_a /= x;
        steps_a++;
        states_a.push_back({curr_a, steps_a});
    }


    vector<pair<long long, int>> states_b;
    long long curr_b = b;
    int steps_b = 0;
    states_b.push_back({curr_b, steps_b});
    while (curr_b > 0) {
        curr_b /= x;
        steps_b++;
        states_b.push_back({curr_b, steps_b});
    }

    long long min_ops = 2e18; 

    
    for (auto& pair_a : states_a) {
        long long val_a = pair_a.first;
        int op_a = pair_a.second;

        for (auto& pair_b : states_b) {
            long long val_b = pair_b.first;
            int op_b = pair_b.second;

            
            long long target = max(val_a, val_b);
            
        
            long long current_ops = op_a + op_b + (target - val_a) + (target - val_b);
            
            min_ops = min(min_ops, current_ops);
        }
    }

    cout << min_ops << "\n";
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