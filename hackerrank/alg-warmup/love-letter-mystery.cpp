#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int my_count(string s) {
    int left = 0;
    unsigned long right = s.length() - 1;
    int cnt = 0;
    while (left < right) {
        cnt += abs(s[left] - s[right]);
        left++;
        right--;
    }
    return cnt;
}

int main() {
    int n;
    string s;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> s;
        cout << my_count(s) << endl;
    }
    return 0;
}