# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/compare-version-numbers/
"""


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def str2lst(self, s):
        if s == '0':
            return [0]
        lst = s.split('.')
        lst = map(int, lst)

        cnt = 0  # 计算末尾0的个数
        while lst[cnt-1] == 0:
            cnt -= 1
        if not cnt:
            return lst
        return lst[:cnt]

    def compareVersion(self, version1, version2):
        v1 = self.str2lst(version1)
        v2 = self.str2lst(version2)
        l = min(len(v1), len(v2))
        for i in xrange(l):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1

        # 前面版本号都相同则比较长短
        if len(v1) < len(v2):
            return -1
        elif len(v1) > len(v2):
            return 1
        return 0

s = Solution()
print s.compareVersion('0.1', '0.0.1')