#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        long long x, y;
        cin >> x >> y;

        long long ans = 0;
        long long b = 1;

        while (b <= y) {
            long long k = x / (b + 1);
            if (k == 0) break;

            long long last = min(y, x / k - 1);

            long long split = k + 1;
            
            long long r1 = min(last, split);
            if (b <= r1) {
                long long n = r1 - b + 1;
                ans += ((b - 1) + (r1 - 1)) * n / 2;
            }

            long long l2 = max(b, split + 1);
            if (l2 <= last) {
                long long n = last - l2 + 1;
                ans += n * k;
            }

            b = last + 1;
        }

        cout << ans << "\n";
    }
}