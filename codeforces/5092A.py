# -*- coding: utf-8 -*-
# Created by mrzero @ 2015-01-31
# http://codeforces.com/contest/509/problem/A
x = int(raw_input())
m = [[1]*x for i in xrange(x)]
for i in xrange(x):
    for j in xrange(x):
        if i == 0 or j == 0:
            continue
        m[i][j] = m[i][j-1] + m[i-1][j]

print m[x-1][x-1]
