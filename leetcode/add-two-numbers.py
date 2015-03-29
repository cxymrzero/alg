# Created by cxy on 15/3/29 with PyCharm
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        num1 = self.convert2Num(l1)
        num2 = self.convert2Num(l2)
        s = num1 + num2
        return self.convert2List(s)

    def convert2Num(self, l):
        num = 0
        num_list = []
        while l:
            num_list.append(l.val)
            l = l.next
        for _ in num_list[::-1]:
            num *= 10
            num += _
        return num

    def convert2List(self, num):
        digit_list = []
        head = ListNode(0)
        while num:
            digit_list.append(num % 10)
            num = num / 10
        if digit_list:
            head = ListNode(digit_list[0])
            tmp = head
            digit_list = digit_list[1:]
            for _ in digit_list:
                tmp.next = ListNode(_)
                tmp = tmp.next
        return head

s = Solution()
print s.convert2List(0)