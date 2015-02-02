# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/palindrome-number/
回文数
"""

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        # 判断数的两端是否相等
        if x < 0:
            return False
        tmp = x
        div1 = -1
        div2 = 0
        while tmp:
            tmp = tmp / 10
            div1 += 1
        while div1 >= div2:
            num1 = (x / 10 ** div1) % 10
            num2 = (x / 10 ** div2) % 10
            if num1 != num2:
                return False
            div1 -= 1
            div2 += 1
        return True


s = Solution()
print s.isPalindrome(13131)
print s.isPalindrome(-1131)