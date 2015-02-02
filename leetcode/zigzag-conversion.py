# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1 or len(s) == 0:
            return s
        res = ''
        for i in range(nRows):
            if i == 0 or i == nRows - 1:
                index = i
                while index < len(s):
                    res += s[index]
                    index += 2 * nRows - 2
            else:
                step = 2 * nRows - 2 - 2 * i
                index = i
                while index < len(s):
                    res += s[index]
                    if index + step < len(s):
                        res += s[index + step]
                    index += 2 * nRows - 2
        return res


s = Solution()
print s.convert('', 1)