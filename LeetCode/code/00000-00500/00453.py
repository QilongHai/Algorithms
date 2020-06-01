from typing import List


class Solution:
    def minMovesNaive(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = 0
        max_idx = n - 1
        count = 0

        while True:
            for idx in range(n):
                if nums[max_idx] < nums[idx]:
                    max_idx = idx
                if nums[min_idx] > nums[idx]:
                    min_idx = idx
            if nums[min_idx] == nums[max_idx]:
                break
            for j in range(n):
                if j != max_idx:
                    nums[j] += 1
            count += 1

        return count

    def minMovesNaiveOpt(self, nums):
        n = len(nums)
        min_idx = 0
        max_idx = n - 1
        count = 0

        while True:
            for i in range(n):
                if nums[max_idx] < nums[i]:
                    max_idx = i
                if nums[min_idx] > nums[i]:
                    min_idx = i
            diff = max_idx - min_idx
            if diff == 0:
                break
            count += diff
            for j in range(n):
                if j != max_idx:
                    nums[j] += diff
        return count

    def minMoves(self, nums):
        moves = 0
        min_ = float('inf')
        for num in nums:
            moves += num
            min_ = min(min_, num)
        return moves - min_ * len(nums)

