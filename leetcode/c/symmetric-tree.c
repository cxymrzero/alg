//
//  symmetric-tree.c
//  c
//  https://leetcode.com/problems/symmetric-tree/
//  Created by mrzero on 15/3/27.
//  Copyright (c) 2015年 cxy. All rights reserved.
//

#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool helper(struct TreeNode *left, struct TreeNode *right) {
    if (left == NULL && right == NULL) {
        return true;
    } else if (left == NULL || right == NULL) {
        return false;
    }
    bool cond1 = left->left->val == right->right->val;
    bool cond2 = helper(left->left, right->right);
    bool cond3 = helper(left->right, right->left);
    return cond1 && cond2 && cond3;
}

bool isSymmetric(struct TreeNode *root) {
    if (root == NULL) {
        return true;
    }
    return helper(root->left, root->right);
}

int main()
{
    printf("hello\n");
    return 0;
}
