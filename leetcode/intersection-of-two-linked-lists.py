# Created by cxy on 15/2/11 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_start_node(head, diff):
    # 找到新的头结点
    cnt = 0
    tmp_node = head
    while cnt < diff:
        tmp_node = tmp_node.next
        cnt += 1
    return tmp_node


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = lenB = 0
        nodeA = tmp = headA

        # 在较长链表取开始结点, 使其到链尾长度与较短链表相等
        while tmp:
            lenA += 1
            tmp = tmp.next
        nodeB = tmp = headB
        while tmp:
            lenB += 1
            tmp = tmp.next
        if lenA > lenB:
            tmp = headA
            nodeA = find_start_node(tmp, lenA - lenB)
        elif lenA < lenB:
            tmp = headB
            nodeB = find_start_node(tmp, lenB - lenA)

        # 开始比较
        while nodeA:
            if nodeA == nodeB and nodeA.next:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next

        return None