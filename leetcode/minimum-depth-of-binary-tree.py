# Created by cxy on 15/2/12 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + self.minDepth(root.right)