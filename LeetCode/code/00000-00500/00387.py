class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in s:
            d[i] = d.get(i, 0) + 1
        for idx, char in enumerate(s):
            if d[char] == 1:
                return idx
        return -1
