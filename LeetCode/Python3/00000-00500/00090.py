from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, tmp + [nums[i]])

        res = []
        n = len(nums)
        nums.sort()
        helper(0, [])
        return res
