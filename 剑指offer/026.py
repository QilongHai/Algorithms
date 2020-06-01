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
