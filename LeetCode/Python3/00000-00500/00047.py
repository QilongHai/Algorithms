from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, tmp_list):
            if not nums:
                res.append(tmp_list)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums[:i] + nums[i + 1:], tmp_list + [nums[i]])

        if not nums:
            return []
        res = []
        nums.sort()
        helper(nums, [])
        return res


class SolutionTwo:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        used = [False for _ in range(n)]
        res = []

        def dfs(depth, path):
            if depth == n:
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(depth + 1, path)
                    used[i] = False
                    path.pop()

        dfs(0, [])
        return res
