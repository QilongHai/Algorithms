from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path[:])
                return
            for idx in range(begin, size):
                cur_val = target - candidates[idx]
                if cur_val < 0:
                    break
                if idx > begin and candidates[idx] == candidates[idx - 1]:
                    continue
                path.append(candidates[idx])
                dfs(candidates, idx + 1, size, path, res, cur_val)
                path.pop()

        size = len(candidates)
        if size == 0:
            return []
        res = []
        path = []
        begin = 0
        candidates.sort()
        dfs(candidates, begin, size, path, res, target)

        return res

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
