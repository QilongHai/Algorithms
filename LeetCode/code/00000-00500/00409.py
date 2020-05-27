class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        d = dict()
        s = s.strip()
        for i in s:
            d[i] = d.get(i, 0) + 1
        res = 0
        odd = 0
        for key, times in d.items():
            if times % 2 == 0:
                res += times
            elif times % 2 == 1:
                odd = 1
                res += times - 1
        if odd == 1:
            return res + 1
        else:
            return res
