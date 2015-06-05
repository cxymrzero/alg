#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll max_index_product(vector<ll> v, vector<ll> *l, vector<ll> *r) {
    unsigned long len = v.size() - 1;
    long long ans = 0;
    long long tmp;

    (*l)[0] = 0;
    (*r)[len-1] = 0;
    
    for (ll i=2; i<=len; i++) {
        ll j = i - 1;
        while (v[j]<=v[i] && j>0) {
            j = (*l)[j];
        }
        (*l)[i] = j;
    }
    
    for (ll i=len-1; i>=1; i--) {
        ll j = i + 1;
        while (v[j]<=v[i] && j>0) {
            j = (*r)[j];
        }
        (*r)[i] = j;
    }
    
    for (int i=1; i<=len; i++) {
        tmp = (*l)[i] * (*r)[i];
        ans = ans>tmp ? ans : tmp;
    }
    
    return ans;
}

int main()
{
    vector<ll> v, l, r;
    ll n, tmp;
    cin >> n;
    
    v.push_back(0);
    l.push_back(0);
    r.push_back(0);
    for (int i=0; i<n; i++) {
        cin >> tmp;
        v.push_back(tmp);
        l.push_back(0);
        r.push_back(0);
    }
    cout << max_index_product(v, &l, &r) << endl;
    return 0;
}