from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(start_node, path_str):
            if start_node:
                path_str += str(start_node.val)
                if not start_node.left and not start_node.right:
                    res.append(path_str)
                else:
                    path_str += '->'
                    if start_node.left:
                        helper(start_node.left, path_str)
                    if start_node.right:
                        helper(start_node.right, path_str)

        if not root:
            return []
        res = []
        path_str = ''
        helper(root, path_str)
        return res
