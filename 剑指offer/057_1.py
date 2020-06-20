from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == target:
                return [nums[i], nums[j]]
            elif tmp > target:
                j -= 1
            else:
                i += 1