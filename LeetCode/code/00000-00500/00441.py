class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        i = 1
        while i <= n:
            n -= i
            i += 1
        return i - 1


class SolutionTwo:
    def arrangeCoins(self, n: int) -> int:
        """根据等差数列求和公式转换而来"""
        return int(((8 * n + 1) ** 0.5 - 1) // 2)