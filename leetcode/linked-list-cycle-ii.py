# Created by cxy on 15/4/1 with PyCharm
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle-ii/
如果链表有环，返回环入口
http://wuchong.me/blog/2014/03/25/interview-link-questions/#
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = fast = head
        has_cycle = False
        # fast每次前进两步，slow每次前进一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # fast回到原点，每次前进一步
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast