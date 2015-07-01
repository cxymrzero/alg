#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool is_palindrome(const string &s) {
    int size = s.size();
    int i = 0, j = size-1;
    while (i <= j) {
        if (s[i++] != s[j--])
            return false;
    }
    return true;
}

bool is_mirror_char(char ch1, char ch2) {
    string s1 = "AEHIJLMOSTUVWXYZ12358";
    string s2 = "A3HILJMO2TUVWXY51SEZ8";
    int n = s1.size();
    for (int i=0; i<n; ++i) {
        if (ch1==s1[i] && ch2==s2[i]) {
            return true;
        }
    }
    return false;
}

bool is_mirror_str(const string &s) {
    int s_size = s.size();
    int i = 0, j = s_size - 1;
    while (i <= j) {
        if (!is_mirror_char(s[i], s[j])) {
            return false;
        }
        ++i; --j;
    }
    return true;
}

void solve(const string &s) {
    bool pal, mirror;
    
    pal = is_palindrome(s);
    mirror = is_mirror_str(s);
    if (!pal && !mirror) {
        cout << s + " -- is not a palindrome.\n" << endl;
    } else if (pal && !mirror) {
        cout << s + " -- is a regular palindrome.\n" << endl;
    } else if (!pal && mirror) {
        cout << s + " -- is a mirrored string.\n" << endl;
    } else {
        cout << s + " -- is a mirrored palindrome.\n" << endl;
    }
}

int main()
{
    string s;
    while (cin >> s) {
        solve(s);
    }
    return 0;
}