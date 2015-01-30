# Created by cxy on 15/1/31 with PyCharm
# -*- coding: utf-8 -*-
i = raw_input()
n, m, k = map(int, i.split(' '))
res = 0
flag = 0
# mt = [[0] * m] * n
mt = [[0] * (m+2) for _ in xrange(n+2)]  # 扩展矩阵成(n+2)*(m+2), 边界置0


def lose(mtx, x, y):
    if mtx[x][y] and mtx[x][y+1] and mtx[x-1][y+1] and mtx[x-1][y] or \
        mtx[x][y] and mtx[x-1][y] and mtx[x-1][y-1] and mtx[x][y-1] or \
        mtx[x][y] and mtx[x][y-1] and mtx[x+1][y-1] and mtx[x+1][y] or \
        mtx[x][y] and mtx[x+1][y] and mtx[x+1][y+1] and mtx[x][y+1]:
        return True
    return False


for l in xrange(k):
    line = raw_input()
    x, y = map(int, line.split(' '))
    mt[x][y] = 1
    if lose(mt, x, y):
        print l + 1
        flag = 1
        break
if not flag:
    print 0