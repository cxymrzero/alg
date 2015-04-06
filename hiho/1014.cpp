#include <iostream>
#include <string>
using namespace std;

struct TreeNode
{
    TreeNode *next[26];
    int cnt;
    TreeNode() {
        cnt = 0;
        for (int i=0; i<26; i++) {
            next[i] = NULL;
        }
    }
};

int main()
{
    TreeNode *t = new TreeNode;
    int m, n;
    cin >> m;

    // 构造Trie树
    string line;
    TreeNode *tmp;
    int index = 0;
    for (int i=0; i<m; i++) {
        cin >> line;
        tmp = t;
        for (int j=0; j<line.size(); j++) {
            index = line[j] - 'a';
            if (tmp->next[index] == NULL) {
                tmp->next[index] = new TreeNode;
            }
            tmp = tmp->next[index];
            tmp->cnt++;
        }
    }

    // 遍历Trie树
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> line;
        tmp = t;
        for (int j=0; j<line.size(); j++) {
            index = line[j] - 'a';
            if (tmp->next[index] == NULL) {
                cout << 0 << endl;
                break;
            }
            tmp = tmp->next[index];
            if (j == line.size()-1) {
                cout << tmp->cnt << endl;
            }
        }
    }
    return 0;
}