# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.res = []

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        self.in_order(root)
        i = 0
        j = len(self.res) - 1
        while i < j:
            if self.res[i] + self.res[j] == k:
                return True
            elif self.res[i] + self.res[j] < k:
                i += 1
            else:
                j -= 1
        return False

    def in_order(self, root):
        if not root:
            return
        if root.left:
            self.in_order(root.left)
        self.res.append(root.val)
        if root.right:
            self.in_order(root.right)
