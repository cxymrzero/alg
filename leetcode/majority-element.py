# Created by cxy on 15/2/11 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/majority-element/
Moore投票算法
参考http://bookshadow.com/weblog/2014/12/22/leetcode-majority-element/
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate = 0
        cnt = 0
        for i in num:
            if cnt == 0:
                candidate = i
                cnt = 1
            elif candidate == i:
                cnt += 1
            else:
                cnt -= 1
        return candidate