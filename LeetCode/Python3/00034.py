# ref: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.search_left(nums, target)
        right_index = self.search_right(nums, target)
        return [left_index, right_index]

    def search_left(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1  # [mid+1, right]
            elif nums[mid] > target:
                right = mid - 1  # [left, mid-1]
            elif nums[mid] == target:
                right = mid - 1
        if left >= n or nums[left] != target:
            return -1
        return left

    def search_right(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1  # [mid+1, right]
            elif nums[mid] > target:
                right = mid - 1  # [left, mid-1]
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right
