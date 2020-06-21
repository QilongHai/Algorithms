from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if pre_sum > 0:
                pre_sum += num
            else:
                pre_sum = num
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum
