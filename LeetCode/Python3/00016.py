from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 3:
            return sum(nums)

        min_diff = float("inf")
        closest_sum = 0
        nums.sort()

        for i in range(length - 2):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                diff = three_sum - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closest_sum = three_sum
                if diff == 0:
                    return closest_sum
                elif diff < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return closest_sum
