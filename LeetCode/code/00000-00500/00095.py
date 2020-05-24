from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            res = []
            for idx in range(start, end + 1):
                left_trees = generate_trees(start, idx - 1)
                right_trees = generate_trees(idx + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        cur_tree = TreeNode(idx)
                        cur_tree.left = left
                        cur_tree.right = right
                        res.append(cur_tree)
                        del cur_tree
            return res

        return generate_trees(1, n) if n else []
