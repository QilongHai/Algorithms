class Solution:
    def titleToNumber(self, string: str) -> int:
        d = dict()
        for i in range(26):
            d[chr(65 + i)] = i + 1
        res = 0
        for s in string:
            res = res * 26 + d[s]
        return res
