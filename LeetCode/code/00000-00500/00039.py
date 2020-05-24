from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def dfs(idx, cur_val, path):
            if cur_val == 0:
                res.append(path[:])
                return
            for j in range(idx, n):
                tmp = cur_val - candidates[j]
                if tmp < 0:
                    break
                path.append(candidates[j])
                dfs(j, tmp, path)
                path.pop()

        dfs(0, target, [])
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


class SolutionFour:
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
            for j in range(idx, n):
                tmp = cur_sum + candidates[j]
                if tmp > target:
                    break
                path.append(candidates[j])
                dfs(j, tmp, path)
                path.pop()

        dfs(0, 0, [])
        return res
