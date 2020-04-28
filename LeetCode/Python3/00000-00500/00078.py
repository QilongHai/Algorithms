from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):
            res.append(path[:])
            for i in range(start, n):
                helper(i + 1, path + [nums[i]])

        res = []
        n = len(nums)
        path = []
        helper(0, path)

        return res
