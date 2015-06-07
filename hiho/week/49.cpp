#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 10000 + 1;
vector<int> g[MAX_N];
int vis[MAX_N] = {};

void dfs(int v) {
    if (vis[v]) return;
    vis[v] = 1;
    for (int i=0; i<g[v].size(); ++i) {
        dfs(g[v][i]);
    }
}

bool solve(int v) {
    dfs(1);
    for (int i=1; i<=v; ++i) {
        if (!vis[i])
            return false;
    }
    return true;
}

int main()
{
    int v, e;
    scanf("%d %d", &v, &e);
    for (int i=0; i<e; ++i) {
        int s, t;
        scanf("%d %d", &s, &t);
        g[s].push_back(t);
        g[t].push_back(s);
    }
    
    // 非连通图
    if (!solve(v)) {
        printf("Part\n");
        return 0;
    }
    
    // 判断奇点个数是否为0或2
    int odd_point_cnt = 0;
    for (int i=1; i<=v; ++i) {
        size_t v_cnt = g[i].size();
        if (v_cnt % 2)
            ++odd_point_cnt;
    }
    if (odd_point_cnt==0 || odd_point_cnt==2) {
        printf("Full\n");
    } else
        printf("Part\n");
    return 0;
}