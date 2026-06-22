#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    vector<long long> st;
    for (int i = 0; i < n; ++i) {
        long long cur = a[i];
        while (!st.empty() && st.back() > cur) {
            cur += st.back();
            st.pop_back();
        }
        st.push_back(cur);
    }

    long long ans = 0;
    for (long long x : st) {
        ans = max(ans, x);
    }
    cout << ans << "\n";
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