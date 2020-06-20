class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        if k > len(s):
            k = len(s) % k
        elif k == len(s):
            return s
        return s[k:] + s[:k]
