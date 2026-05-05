#include<iostream>
using namespace std;

int main() {
    int t, x;
    cin >> t;

    while(t--) {
        cin >> x;

        if (x < 67) {
            cout << x + 1 << endl;
        }
        else {
            cout << x << endl;
        }
    }
    return 0;
}