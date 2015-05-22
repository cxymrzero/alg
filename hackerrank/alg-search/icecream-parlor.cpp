#include <vector>
#include <iostream>
using namespace std;


int main() {
    int t, m, n, tmp, done = false;
    vector<int> v;
    
    cin >> t;
    for (int i=0; i<t; i++) {
        done = false;
        cin >> m >> n;
        v.clear();
        for (int j=0; j<n; j++) {
            cin >> tmp;
            v.push_back(tmp);
        }
        
        for (int i=0; i<n; i++) {
            if (done) break;
            for (int j=i+1; j<n; j++) {
                if (v[i]+v[j] == m) {
                    cout << i+1 << " " << j+1 <<endl;
                    done = true;
                    break;
                }
            }
        }
    }
    
    return 0;
}