# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> int:
        if not root:
            return 0
        stack = [(root, [root.val])]
        res = 0
        while stack:
            node, tmp = stack.pop()
            res += tmp.count(target_sum)
            tmp += [0]
            if node.left:
                array = [i + node.left.val for i in tmp]
                stack.append((node.left, array))
            if node.right:
                array = [j + node.right.val for j in tmp]
                stack.append((node.right, array))
        return res
