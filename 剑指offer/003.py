from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            while idx != nums[idx]:
                val = nums[idx]
                if val != nums[val]:
                    nums[idx], nums[val] = nums[val], nums[idx]
                else:
                    return val
        return -1