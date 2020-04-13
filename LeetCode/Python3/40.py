from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(start, path, target):
            if target == 0:
                res.append(path[:])
                return

            for idx in range(start, size):
                if candidates[idx] > target:
                    break

                if idx > start and candidates[idx - 1] == candidates[idx]:
                    continue

                path.append(candidates[idx])
                dfs(idx + 1, path, target - candidates[idx])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
