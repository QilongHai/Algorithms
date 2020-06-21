from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, pre_order: List[int], in_order: List[int]) -> TreeNode:
        if not pre_order:
            return None
        root = TreeNode(pre_order[0])
        index = in_order.index(pre_order[0])
        root.left = self.buildTree(pre_order[1:index + 1], in_order[:index])
        root.right = self.buildTree(pre_order[index + 1:], in_order[index + 1:])
        return root
