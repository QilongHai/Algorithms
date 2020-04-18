# ref: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        q = 1
        n = len(nums)
        if n < 2:
            return n
        while q < n:
            if nums[p] == nums[q]:
                q += 1
            else:
                if q - p > 1:
                    nums[p + 1] = nums[q]
                p += 1
                q += 1
        return p + 1
