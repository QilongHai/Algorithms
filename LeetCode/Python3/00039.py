from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, res, path, target):
            if target == 0:
                res.append(path[:])
                return
            for index in range(begin, size):
                cur_val = target - candidates[index]
                if cur_val < 0:
                    break
                path.append(candidates[index])
                dfs(candidates, index, size, res, path, cur_val)
                path.pop()

        size = len(candidates)
        if size == 0:
            return []        
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, res, path, target)

        return res
