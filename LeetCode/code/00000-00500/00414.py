from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums.sort()
        return nums[-3]


class SolutionTwo:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        if len(nums) < 3:
            return max(nums)
        for num in nums:
            if num > third:
                if num < second:
                    third = num
                elif num > second:
                    if num < first:
                        third = second
                        second = num
                    elif num > first:
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third


