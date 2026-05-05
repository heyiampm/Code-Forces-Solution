#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;
    int n = s.length();
    vector<int> pi(n, 0);
    int max_mid = 0;

    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
        
        if (i < n - 1) {
            max_mid = max(max_mid, pi[i]);
        }
    }

    int res = pi[n - 1];

    while (res > max_mid) {
        res = pi[res - 1];
    }

    if (res <= 0) {
        cout << "Just a legend" << "\n";
    } else {
        cout << s.substr(0, res) << "\n";
    }

    return 0;
}