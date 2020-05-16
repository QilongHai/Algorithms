from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)

        in_order(root)
        return res


class SolutionTwo:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right()
        return res


class SolutionThree:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                if stack:
                    root = stack.pop()
                    res.append(root.val)
                    root = root.right
        return res
