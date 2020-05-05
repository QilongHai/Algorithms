from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tmp_set = set()
        for item in wordDict:
            tmp_set.add(item)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i]表示s的前i位是否可以用wordDict中的单词表示
        dp[0] = True  # 空字符串
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in tmp_set):
                    dp[j] = True
        return dp[-1]
