from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        new_index = 0
        for num in nums:
            if num == val:
                continue
            else:
                nums[new_index] = num
                new_index += 1
        return new_index
