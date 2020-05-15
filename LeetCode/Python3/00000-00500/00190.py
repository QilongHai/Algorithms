class Solution:
    def reverseBits(self, n: int) -> int:
        stack = [0 for _ in range(32)]
        i = 31
        while i >= 0:
            stack[i] = n & 1
            n >>= 1
            i -= 1
        res = 0
        for j in stack[::-1]:
            res = res * 2 + j
        return res
