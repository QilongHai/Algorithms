from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums) - 1
        p = -1
        p_val = 0
        for i in range(n - 1, -1, 0):
            if nums[i] < nums[i + 1]:
                p = i
                p_val = nums[i]
                break
        if p == -1:
            self.my_reverse(nums, 0, n)
            return
        for j in range(n, -1, -1):
            if nums[j] > p_val:
                nums[j], nums[p] = nums[p], nums[j]
                break
        self.my_reverse(nums, p + 1, n)

    def my_reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
