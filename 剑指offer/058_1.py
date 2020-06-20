class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        res = []
        for i in s:
            if i:
                res.append(i)
        return ' '.join(res[::-1])