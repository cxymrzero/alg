# Created by cxy on 15/2/11 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/pascals-triangle/
"""
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        nums = []
        for i in xrange(numRows):
            nums.append([])
            for j in xrange(i + 1):
                if j == 0 or j == i:
                    nums[i].append(1)
                else:
                    nums[i].append(nums[i-1][j-1] + nums[i-1][j])
        return nums


s = Solution()
print s.generate(5)