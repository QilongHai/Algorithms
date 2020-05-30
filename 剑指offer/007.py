from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left_pre = preorder[1:index+1]
        left_in = inorder[:index]
        right_pre = preorder[index+1:]
        right_in = inorder[index+1:]

        node.left = self.buildTree(left_pre, left_in)
        node.right = self.buildTree(right_pre, right_in)

        return node
