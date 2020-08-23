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


class SolutionTwo:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx == num:
                continue
            else:
                if num == nums[num]:
                    return num
                else:
                    nums[idx], nums[num] = nums[num], nums[idx]
        return -1
