from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[::-1]
        self.swap(nums, 0, k - 1)
        self.swap(nums, k, n - 1)

    def swap(self, array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
# 原始数组                  : 1 2 3 4 5 6 7
# 反转所有数字后             : 7 6 5 4 3 2 1
# 反转前 k 个数字后          : 5 6 7 4 3 2 1
# 反转后 n-k 个数字后        : 5 6 7 1 2 3 4
