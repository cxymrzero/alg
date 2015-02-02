# Created by cxy on 15/2/2 with PyCharm
# -*- coding: utf-8 -*-


class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x
        elif x > 0:
            sign = 0
            v = x
        else:
            sign = 1
            v = -x

        tmp = 0
        while v:
            a = v / 10
            b = v % 10
            tmp = tmp * 10 + b
            # 考虑溢出
            if tmp < -0x7fffffff or 0x7fffffff < tmp:
                return 0
            v = a
        if sign:
            return -tmp
        return tmp


s = Solution()
print s.reverse(123)