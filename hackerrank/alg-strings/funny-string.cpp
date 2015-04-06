#include <iostream>
#include <string>
#include <cstdbool>

using namespace std;

bool is_funny(string s) {
    int i = 0;
    unsigned long j = s.length() - 1;
    
    if (s.length() == 1) {
        return true;
    }
    
    while (i < j-1) {
        if (abs(s[i]-s[i+1]) != abs(s[j-1]-s[j])) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    int n;
    string s;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> s;
        if (is_funny(s)) {
            cout << "Funny" << endl;
        } else {
            cout << "Not Funny" << endl;
        }
    }
    return 0;
}