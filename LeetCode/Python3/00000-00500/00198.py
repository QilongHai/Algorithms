from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i]表示到第i个房屋的偷窃最高金额
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1]) 
        return dp[-1]

