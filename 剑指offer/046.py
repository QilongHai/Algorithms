class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            if '10' <= s[i - 2:i] <= '25':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[n]
