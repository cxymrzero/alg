# Created by cxy on 15/2/12 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
层序遍历二叉树
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queues = [[], []]
        tmp_queue = 0
        tmp_node = root
        cnt = 0
        queues[tmp_queue].append(tmp_node)
        while tmp_node:
            cnt += 1
            if tmp_node.left:
                queues[1-tmp_queue].append(tmp_node.left)
            if tmp_node.right:
                queues[1-tmp_queue].append(tmp_node.right)
            if cnt == len(queues[tmp_queue]):
                level_res = [node.val for node in queues[tmp_queue]]
                res.append(level_res)
                if not queues[1-tmp_queue]:
                    return res
                queues[tmp_queue] = []
                tmp_node = queues[1-tmp_queue][0]
                tmp_queue = 1 - tmp_queue
                cnt = 0
            else:
                tmp_node = queues[tmp_queue][cnt]
        return res