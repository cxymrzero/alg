# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/factorial-trailing-zeroes/
算出1-n范围内元素5出现的次数
"""

def five_power(n):
    s = 1
    while True:
        if n < 5 ** s:
            return s - 1
        s += 1


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        t = five_power(n)
        sum = 0
        for i in xrange(1, t+1):
            sum += n / 5 ** i
        return sum

s = Solution()
print s.trailingZeroes(8425)