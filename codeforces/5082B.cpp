#include <iostream>
#include <string.h>

using namespace std;

string my_swap(string s, int i) {
    string tmp = s;
    tmp[s.length()-1] = s[i];
    tmp[i] = s[s.length()-1];
    return tmp;
}

int main() {
    int last_even = -1;
    int small_even = -1;
    string s;
    string res;
    cin >> s;
    int len = s.length();
    int n[len];
    int last = s[len-1] - '0';
    int index = -1;

    // 如果找到比末位小的偶数, 则用这个偶数; 否则用最后一个偶数
    for (int i=0; i<len; i++) {
        int tmp = 0;
        tmp = n[i] = s[i] - '0';
        if (tmp % 2 == 0) {
            if (tmp > last) {
                last_even = i;
            } else if (small_even == -1) {
                small_even = i;
                break;
            }
        }
    }

    if (small_even != -1) {
        index = small_even;
    } else if (last_even != -1) {
        index = last_even;
    } else {
        cout << -1 << endl;
        return 0;
    }

    cout << my_swap(s, index) << endl;
    return 0;
}
