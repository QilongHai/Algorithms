class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                if dp[i] > max_len:
                    max_len = dp[i]
        return max_len