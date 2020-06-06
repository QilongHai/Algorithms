from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            mid = i + (j - i) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                j = mid
            else:
                i = mid + 1
        return i