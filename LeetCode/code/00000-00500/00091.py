class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or not s:
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if s[1] != '0':  #  看第二个字母是否为0
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, n):
            if s[i - 1] == '0' and s[i] == '0':
                return 0
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
