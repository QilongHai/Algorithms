from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, stop, path, res, target):
            if target == 0:
                res.append(list(path))
                return

            for idx in range(begin, stop):
                val = target - candidates[idx]
                if val < 0:
                    break
                path.append(candidates[idx])
                # 因为下一层不能比上一层还小，起始索引还从 index 开始
                dfs(candidates, idx, stop, path, res, val)
                path.pop()

        if not candidates:
            return []
        candidates.sort()
        path = []
        res = []
        size = len(candidates)
        dfs(candidates, 0, size, path, res, target)
        return res
