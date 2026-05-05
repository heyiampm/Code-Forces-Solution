#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    int x1 = s[0], y1 = s[1];
    int x2 = t[0], y2 = t[1];
    int moves = max(abs(x1 - x2), abs(y1 - y2));
    cout << moves << endl;
    while (x1 != x2 || y1 != y2) {
        string step = "";
        if (x1 < x2) {
            step += 'R';
            x1++;
        } else if (x1 > x2) {
            step += 'L';
            x1--;
        }
        if (y1 < y2) {
            step += 'U';
            y1++;
        } else if (y1 > y2) {
            step += 'D';
            y1--;
        }
        cout << step << endl;
    }

    return 0;
}