from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_sum = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit_sum += tmp
        return profit_sum