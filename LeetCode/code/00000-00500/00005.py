# ref: https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/


class Solution:

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1
        start = 0
        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                dis = j - i
                if s[i] == s[j]:
                    if dis < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = dis + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


class SolutionTwo:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        res = s[0]

        for i in range(n):
            odd_str, odd_len = self.center_spread(s, n, i, i)
            even_str, even_len = self.center_spread(s, n, i, i + 1)
            cur_max_sub_str = odd_str if odd_len >= even_len else even_str
            if len(cur_max_sub_str) > max_len:
                max_len = len(cur_max_sub_str)
                res = cur_max_sub_str
        return res

    @staticmethod
    def center_spread(s, size, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i + 1
