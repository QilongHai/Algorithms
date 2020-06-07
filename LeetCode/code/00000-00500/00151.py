class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        tmp = s.strip().split()
        stack = [item for item in tmp if item]
        res = ' '.join(stack[::-1])
        return res