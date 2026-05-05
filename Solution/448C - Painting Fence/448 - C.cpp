#include <bits/stdc++.h>
using namespace std;

const int N = 5005;
int a[N];

int solve(int l, int r, int h) {
    if (l > r) return 0;

    int mn = a[l];
    for (int i = l; i <= r; i++) {
        mn = min(mn, a[i]);
    }

    int horizontal = mn - h;

    int i = l;
    while (i <= r) {
        if (a[i] == mn) {
            i++;
            continue;
        }

        int j = i;
        while (j <= r && a[j] != mn) j++;

        horizontal += solve(i, j - 1, mn);
        i = j;
    }

    int vertical = r - l + 1;

    return min(vertical, horizontal);
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << solve(0, n - 1, 0) << endl;

    return 0;
}