from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        idx = 0
        while idx < len(nums):
            cur_str = str(nums[idx])
            pos = idx
            while (idx < len(nums) - 1) and (nums[idx] + 1 == nums[idx + 1]):
                idx += 1
            if pos != idx:
                cur_str = cur_str + '->' + str(nums[idx])
            res.append(cur_str)
            idx += 1
        return res
