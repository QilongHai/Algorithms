import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return ''
            ans = '#'.join((str(node.val), dfs(node.left), dfs(node.right)))
            d[ans].append(node)
            return ans

        d = collections.defaultdict(list)
        dfs(root)

        return [item[0] for item in d.values() if len(item) > 1]
