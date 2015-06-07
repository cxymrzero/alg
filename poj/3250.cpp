// 单调栈，小心爆int
#include <cstdio>
#include <iostream>
#include <stack>

using namespace std;

typedef long long ll;

int main()
{
    ll N, res = 0;
    scanf("%lld", &N);
    
    stack<ll> s;
    for (ll i=0; i<N; ++i) {
        ll h;
        scanf("%lld", &h);
        while (!s.empty() && s.top()<=h)
            s.pop();
        res += s.size();
        s.push(h);
    }
    printf("%lld\n", res);
    return 0;
}