# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/excel-sheet-column-title/
本质是进制转换, 要处理好除数和余数的关系, 考虑为0的情况
"""


class Solution:
    # @return a string
    d = {}
    for i in range(1, 27):
        d[i] = chr(ord('A') + i - 1)
        d[0] = ''

    def convertToTitle(self, num):
        res = ''
        tmp = num
        while tmp:
            a = tmp / 26
            b = tmp % 26
            if b == 0:
                a -= 1
                b = 26
            res += self.d[b]
            tmp = a
        return res[::-1]

s = Solution()
print s.convertToTitle(2)
print s.convertToTitle(26)