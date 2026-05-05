#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;
vector<int> pos[5001];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= 2 * n; i++) {
        int val;
        cin >> val;
        pos[val].push_back(i); 
    }
    for (int i = 1; i <= 5000; i++) {
        if (pos[i].size() % 2 != 0) {
            cout << -1 << endl;
            return 0;
        }
    }

    for (int i = 1; i <= 5000; i++) {
        for (int j = 0; j < pos[i].size(); j += 2) {
            cout << pos[i][j] << " " << pos[i][j+1] << "\n";
        }
    }

    return 0;
}