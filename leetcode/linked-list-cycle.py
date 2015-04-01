# Created by cxy on 15/4/1 with PyCharm
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle/
判断链表中是否存在环
用两个指针，一个每次前移1个结点，一个每次前移两个。若有环，则两个指针必会相遇。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        ptr1 = ptr2 = head
        while ptr2:
            if ptr2.next and ptr2.next.next:
                ptr2 = ptr2.next.next
            else:
                break
            if ptr1.next:
                ptr1 = ptr1.next
            else:
                break
            if ptr1 == ptr2:
                return True
        return False