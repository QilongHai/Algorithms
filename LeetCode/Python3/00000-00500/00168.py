class Solution:
    def convertToTitle(self, n: int) -> str:
        d = dict()
        for i in range(26):
            d[i + 1] = chr(ord('A') + i)
        d[0] = 'Z'
        stack = []
        while n:
            mod = n % 26
            if mod == 0:
                n -= 26
            stack.append(mod)
            n //= 26
        res = ''
        for i in stack:
            res += d[i]
        return res[::-1]
