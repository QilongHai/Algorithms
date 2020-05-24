from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        n = len(nums)
        half = n // 2
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > half:
                return num
