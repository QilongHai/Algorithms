from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start_idx, path, cur_target):
            if cur_target == 0:
                res.append(path[:])
                return
            for j in range(start_idx, size):
                cur_val = cur_target - candidates[j]
                if cur_val < 0:
                    break
                path.append(candidates[j])
                dfs(j, path, cur_val)
                path.pop()

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        dfs(0, [], target)

        return res


class SolutionTwo:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(idx, cur_sum, path):
            if cur_sum > target or idx == n:
                return
            if cur_sum == target:
                res.append(path[:])
                return
            dfs(idx, cur_sum + candidates[idx], path + [candidates[idx]])
            dfs(idx + 1, cur_sum, path)

        dfs(0, 0, [])
        return res


class SolutionThree:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(idx, cur_sum, path):
            if idx >= n or cur_sum > target:
                return
            if cur_sum == target:
                res.append(path[:])
                return
            for j in range(idx, n):
                if candidates[j] + cur_sum > target:
                    break
                dfs(j, candidates[j] + cur_sum, [candidates[j]] + path)

        dfs(0, 0, [])
        return res
