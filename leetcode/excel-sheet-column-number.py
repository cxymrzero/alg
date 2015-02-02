# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in xrange(len(s)):
            res = res * 26 + (ord(s[i]) - ord('A') + 1)
        return res

s = Solution()
print s.titleToNumber('ZA')