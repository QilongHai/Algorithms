from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        return dp[n-1][0]


class SolutionTwo:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        dp_0 = 0
        dp_1 = -prices[0] - fee
        for i in range(1, n):
            yesterday_dp_0 = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, yesterday_dp_0 - prices[i] - fee)
        return dp_0
