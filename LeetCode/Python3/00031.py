from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        p = -1
        q = 0
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                p = i
            if p != -1 and nums[i] > nums[p]:
                q = i
        if p != -1 and nums[-1] > nums[p]:
            q = n - 1
        if p == -1:
            nums[:] = nums[::-1]
        else:
            nums[p], nums[q] = nums[q], nums[p]
            nums[:] = nums[:p+1] + nums[n-1:p:-1]



