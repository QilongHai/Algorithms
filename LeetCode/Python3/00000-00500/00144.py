from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def pre_order(root):
            if not root:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return res


class SolutionTwo:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
