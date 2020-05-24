from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        level = 0
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                cur_node = q.popleft()
                if cur_node:
                    tmp.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
            if tmp:
                if level % 2:
                    res.append(tmp[::-1])
                else:
                    res.append(tmp)
            level += 1
        return res
