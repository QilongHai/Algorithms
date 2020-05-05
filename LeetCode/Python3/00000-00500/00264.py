class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        two = 0
        three = 0
        five = 0
        for i in range(1, n):
            ugly_num = min(dp[two] * 2, dp[three] * 3, dp[five] * 5)
            dp[i] = ugly_num
            if ugly_num == dp[two] * 2:
                two += 1
            if ugly_num == dp[three] * 3:
                three += 1
            if ugly_num == dp[five] * 5:
                five += 1
        return dp[-1]
