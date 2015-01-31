# Created by cxy on 15/1/31 with PyCharm
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/508/B greedy
l = raw_input()


def find(s):
    last_even = -1
    tmp = []
    last = int(s[-1])
    small_even = -1

    for i in xrange(len(s)):
        n = int(s[i])
        if n % 2 == 0:
            last_even = i
            if small_even == -1 and n < last:
                small_even = i
        tmp.append(n)

    if small_even != -1:
        res = small_even
    elif last_even != -1:
        res = last_even
    else:
        return -1

    tmp[res], tmp[-1] = tmp[-1], tmp[res]

    ret = 0
    j = -1
    for i in xrange(len(tmp)):
        ret = tmp[j] * 10 ** i + ret
        j -= 1
    return ret


print find(l)