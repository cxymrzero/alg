#include <iostream>

using namespace std;

int max_xor(int l, int r) {
    int res = 0, tmp;
    for (int i=l; i<=r; i++) {
        for (int j=i; j<=r; j++) {
            tmp = i ^ j;
            res = res > tmp ? res : tmp;
        }
    }
    return res;
}

int main() {
    int l, j;
    cin >> l >> j;
    cout << max_xor(l, j);
    return 0;
}