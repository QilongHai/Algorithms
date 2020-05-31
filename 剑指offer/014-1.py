class Solution:
    def cuttingRopeRecursion(self, n: int) -> int:
        """
        设 F(n) 为长度为 n 的绳子可以得到的最大乘积
        F(n) = max(i*(n−i), i*F(n−i)), i=1, 2, ..., n−2
        """
        if n == 2:
            return 1
        res = -1
        for i in range(1, n):
            res = max(res, max(i * self.cuttingRopeRecursion(n-i), i * (n - i)))
        return res

    def cuttingRope_dp(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i-j]))
        return dp[n]

        
