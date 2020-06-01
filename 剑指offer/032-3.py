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
        queue = deque()
        queue.append(root)
        level = 1
        res = []
        while queue:
            n = len(queue)
            ans = []
            for _ in range(n):
                cur_node = queue.popleft()
                if cur_node:
                    ans.append(cur_node.val)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
            if ans:
                if level % 2:
                    res.append(ans)
                else:
                    res.append(ans[::-1])
                level += 1
        return res
