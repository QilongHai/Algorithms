class Solution:
    def isSubStructure(self, A, B):
        def helper(A, B):
            if not B:
                return True
            if not A:
                return False
            if A.val != B.val:
                return False
            return helper(A.left, B.left) and helper(A.right, B.right)

        if not A or not B:
            return False
        return helper(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionTwo:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def dfs(self, a, b):
        if not b:
            return True
        if not a:
            return False
        return a.val == b.val and self.dfs(a.left, b.left) and self.dfs(a.right, b.right)
