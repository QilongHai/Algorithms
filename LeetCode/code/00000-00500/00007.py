class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        sign = 1 if x > 0 else -1
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= sign
        if -pow(2, 31) <= res <= pow(2, 31) - 1:
            return res
        else:
            return 0
