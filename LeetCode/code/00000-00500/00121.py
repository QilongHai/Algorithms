from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


class SolutionTwo:
    """
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                max(   选择 rest  ,           选择 sell      )

    解释：今天我没有持有股票，有两种可能：
    要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
    要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。

    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                max(   选择 rest  ,           选择 buy         )

    解释：今天我持有着股票，有两种可能：
    要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
    要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[i-1][0]


class SolutionThree:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_0 = 0
        dp_1 = float('-inf')
        for i in range(n):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, -prices[i])
        return dp_0


