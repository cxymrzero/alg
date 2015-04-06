#include <iostream>

using namespace std;

int height(int year) {
    int h = 1;
    for (int i=0; i<year; i++) {
        if (i%2 == 0) {
            h *= 2;
        } else {
            h++;
        }
    }
    return h;
}

int main() {
    int cnt;
    int year;
    cin >> cnt;
    for (int i=0; i<cnt; i++) {
        cin >> year;
        cout << height(year) << endl;
    }
    return 0;
}