#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        long long n, a, b;
        cin >> n >> a >> b;

        long long result;

        if (3 * a <= b) {
            result = n * a;
        } else {
            long long groups = n / 3;
            long long rem = n % 3;

            result = groups * b + min(rem * a, b);
        }

        cout << result << "\n";
    }

    return 0;
}