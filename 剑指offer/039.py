from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        res = None
        for num in nums:
            if votes == 0:
                res = num
            if num == res:
                votes += 1
            else:
                votes -= 1
        return res
