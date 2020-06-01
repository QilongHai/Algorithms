from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(len(nums)):
            new_idx = abs(nums[idx]) - 1
            if nums[new_idx] > 0:
                nums[new_idx] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)
        return res
