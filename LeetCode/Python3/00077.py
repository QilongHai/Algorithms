# ref: https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, k, n, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            else:
                for i in range(start, n + 1):
                    path.append(i)
                    dfs(i + 1, k, n, path, res)
                    path.pop()

        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        path = []
        start = 1
        dfs(start, k, n, path, res)

        return res
