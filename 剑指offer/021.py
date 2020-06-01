from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        i = 0
        j = len(nums) - 1
        for item in nums:
            if item % 2 == 0:
                res[j] = item
                j -= 1
            else:
                res[i] = item
                i += 1
        return res

    def exchange_two(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2:
                i += 1
            while i < j and not nums[i] % 2:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
