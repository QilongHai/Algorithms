from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                count += 1
        for k in range(len(nums) - 1, len(nums) - 1 - count, -1):
            nums[k] = 0
