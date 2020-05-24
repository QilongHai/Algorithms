from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                    for item in cur.children:
                        q.append(item)
            if tmp:
                res.append(tmp)
        return res
