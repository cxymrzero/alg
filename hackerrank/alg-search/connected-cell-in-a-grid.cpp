#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

typedef struct Node {
    int v;
    int i;
    int j;
    bool visited = false;
} Node;

void push_node(Node *node, stack<Node> *s) {
    if (!node->visited) {
        node->visited = true;
        if (node->v == 1) {
            (*s).push(*node);
        }
    }
}

int main() {
    int m, n;
    cin >> m >> n;
    m+=2;
    n+=2;
    Node *matrix = new Node[m*n];  // 一维模拟二维，补一圈边界
    Node *tmp_node;
    
    // 覆盖边界
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            tmp_node = &matrix[i*n+j];
            tmp_node->i = i;
            tmp_node->j = j;
            tmp_node->visited = true;
        }
    }
    
    // 读矩阵
    for (int i=1; i<m-1; i++) {
        for (int j=1; j<n-1; j++) {
            tmp_node = &matrix[i*n+j];
            cin >> tmp_node->v;
            tmp_node->visited = false;
        }
    }
    
    stack<Node> s;
    Node top_node;
    int ans = 0, cnt = 0;
    int x, y;
    Node *next_nodes[8];
    for (int i=0; i<8; i++) {
        next_nodes[i] = new Node;
    }
    
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            tmp_node = &matrix[i*n+j];
            if (tmp_node->visited || tmp_node->v==0) {
                continue;
            }
            s.push(*tmp_node);
            cnt = 0;
            tmp_node->visited = true;
            while (!s.empty()) {
                top_node = s.top();
                s.pop();
                cnt++;

                x = top_node.i;
                y = top_node.j;

                // 8个相邻结点
                next_nodes[0] = &matrix[(x-1)*n+(y-1)]; //左上
                next_nodes[1] = &matrix[(x-1)*n+y];     //上
                next_nodes[2] = &matrix[(x-1)*n+(y+1)]; //右上
                next_nodes[3] = &matrix[x*n+(y-1)];     //左
                next_nodes[4] = &matrix[x*n+(y+1)];     //右
                next_nodes[5] = &matrix[(x+1)*n+(y-1)]; //左下
                next_nodes[6] = &matrix[(x+1)*n+y];     //下
                next_nodes[7] = &matrix[(x+1)*n+(y+1)]; //右下
                
                for (int i=0; i<8; i++) {
                    push_node(next_nodes[i], &s);
                }
            }
            ans = max(ans, cnt);
        }
    }
    
    cout << ans << endl;
    return 0;
}