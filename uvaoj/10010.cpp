#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string mat[50];
int m, n;
// 左，左上，上，右上，右，右下，下，左下
int row_dir[] = {0, -1, -1, -1, 0, 1, 1, 1};
int col_dir[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int DIR = 8;

bool dir_ok(int row, int col, int dir, int word_len, const string &s) {
    int x, y, i;
    for (i=0; i<word_len; ++i) {
        x = row + i * row_dir[dir];
        y = col + i * col_dir[dir];
        if (x<0 || x>=m || y<0 || y>=n || mat[x][y]!=s[i]) {
            break;
        }
    }
    return i == word_len;
}

void solve(const string &s) {
    int len = s.length();
    for (int i=0; i<m; ++i) {
        for (int j=0; j<n; ++j) {
            for (int dir=0; dir<DIR; ++dir) {
                if (dir_ok(i, j, dir, len, s)) {
                    printf("%d %d\n", i+1, j+1);
                    return;
                }
            }
        }
    }
}

void s_tolower(string &s) {
    for (auto it=s.begin(); it!=s.end(); ++it) {
        *it = tolower(*it);
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; ++i) {
        scanf("%d %d", &m, &n);
        for (int j=0; j<m; ++j) {
            cin >> mat[j];
            s_tolower(mat[j]);
        }
        
        int case_cnt;
        string s;
        scanf("%d", &case_cnt);
        for (int k=0; k<case_cnt; ++k) {
            cin >> s;
            s_tolower(s);
            solve(s);
        }
        if (i != N-1)
            printf("\n");
    }
    return 0;
}