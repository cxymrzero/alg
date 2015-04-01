# Created by cxy on 15/3/30 with PyCharm
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        tmp = p.next

        while p.next:
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if p.next == tmp:
                p = p.next
                tmp = tmp.next
            else:
                p.next = tmp.next
        return dummy.next