from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp_list):
            if not nums:
                res.append(tmp_list)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp_list + [nums[i]])

        if not nums:
            return []
        res = []
        backtrack(nums, [])
        return res


class SolutionTwo:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        hash_set = set()

        def backtrack(depth, path):
            if depth == n:
                res.append(path[:])
                return
            for i in range(n):
                if nums[i] not in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])
                    backtrack(depth + 1, path)
                    path.pop()
                    hash_set.remove(nums[i])

        backtrack(0, [])
        return res


class SolutionThree:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False for _ in range(n)]

        def backtrack(depth, path):
            if depth == n:
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(depth+1, path)
                    path.pop()
                    used[i] = False

        backtrack(0, [])
        return res


