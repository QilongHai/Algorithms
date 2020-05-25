class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.left_leaves_sum(root, False)

    def left_leaves_sum(self, root, is_left_leave):
        if not root:
            return 0
        if not root.left and not root.right and is_left_leave:
            return root.val
        else:
            return self.left_leaves_sum(root.left, True) + self.left_leaves_sum(root.right, False)
