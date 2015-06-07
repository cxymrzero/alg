// 通过压缩矩阵将二维问题转化为最大子序列和问题求解

#include <cstdio>
#include <iostream>

using namespace std;

const int MAX_N = 100;
int mat[MAX_N][MAX_N], tmp[MAX_N] = {};

void compress_matrix(int beg, int end, int N) {
    for (int i=0; i<N; ++i) {
        int s = 0;
        for (int j=beg; j<=end; ++j) {
            s += mat[j][i];
        }
        tmp[i] = s;
    }
}

int max_subarray_sum(int N) {
    int s = 0, m = 0;
    for (int i=0; i<N; ++i) {
        s += tmp[i];
        if (s < 0)
            s = 0;
        else if (s > m)
            m = s;
    }
    return m;
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; ++i) {
        for (int j=0; j<N; ++j) {
            scanf("%d", &mat[i][j]);
        }
    }
    int res = 0;
    for (int i=0; i<N; ++i) {
        for (int j=i; j<N; ++j) {
            compress_matrix(i, j, N);
            res = max(max_subarray_sum(N), res);
        }
    }
    printf("%d\n", res);
    return 0;
}