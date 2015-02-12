# Created by cxy on 15/2/12 with PyCharm
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/path-sum/
DFS遍历树
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if root.left:
            if self.hasPathSum(root.left, sum-root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, sum-root.val):
                return True
        if not root.left and not root.right:
            if root.val == sum:
                return True
        return False