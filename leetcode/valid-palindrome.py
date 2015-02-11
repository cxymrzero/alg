# Created by cxy on 15/2/11 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/valid-palindrome/
"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        s = s.lower()
        index1 = 0
        index2 = len(s) - 1
        while index1 < index2:
            if not s[index1].isalnum():
                index1 += 1
                continue
            if not s[index2].isalnum():
                index2 -= 1
                continue
            if s[index1] != s[index2]:
                return False
            index1 += 1
            index2 -= 1
        return True