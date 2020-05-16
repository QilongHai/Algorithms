from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, root)

    def helper(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.helper(p.left, q.right) and self.helper(p.right, q.left)


class SolutionTwo:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append(root)
        queue.append(root)
        while len(queue) > 0:
            p = queue.popleft()
            q = queue.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(q.left)
            queue.append(p.right)
        return True
