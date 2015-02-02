# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/string-to-integer-atoi/
这题要判断的条件太多了...
"""


class Solution:
    # @return an integer
    def atoi(self, str):
        sign = 0
        str = str.strip(' ')
        if not str:
            return 0
        if len(str) > 1 and (str[0] == '-' or str[0] == '+'):
            if str[0] == '-':
                sign = 1
            str = str[1:]

        sum = 0
        for c in str:
            if not c in "1234567890":
                break
            sum = sum * 10 + ord(c) - ord('0')

        if sign:
            sum = -sum

        # 溢出
        if sum > 0x7fffffff:
            return 0x7fffffff
        elif sum < -0x80000000:
            return -0x80000000
        else:
            return sum


s = Solution()
print s.atoi('-123')