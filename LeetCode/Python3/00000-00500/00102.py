from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                cur = q.popleft()
                if cur:
                    tmp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if tmp:
                res.append(tmp)
        return res
