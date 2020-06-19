from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        joker_count = 0
        for i in range(4):
            if nums[i] == 0:
                joker_count += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker_count] < 5
