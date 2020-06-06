from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


class SolutionTwo:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        tail = [nums[0]]
        for i in range(1, n):
            left = 0
            right = len(tail)
            while left < right:
                mid = left + (right - left) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tail):
                tail.append(nums[i])
            else:
                tail[left] = nums[i]
        
        return len(tail)
