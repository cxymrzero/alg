# Created by cxy on 15/2/12 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/pascals-triangle-ii/
利用杨辉三角中的组合数规律
"""


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n - 1) * n


def combine(m, n):
    # 求组合Cm取n
    return fac(m) / (fac(n) * fac(m - n))


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = []
        for i in xrange(rowIndex+1):
            res.append(combine(rowIndex, i))
        return res

s = Solution()
print s.getRow(3)