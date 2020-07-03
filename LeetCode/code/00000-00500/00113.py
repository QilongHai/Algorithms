from .utils import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, cur_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == cur_sum:
                res.append(path.copy())
            dfs(node.left, path, cur_sum - node.val)
            dfs(node.right, path, cur_sum - node.val)
            path.pop()

        dfs(root, [], target_sum)
        return res
