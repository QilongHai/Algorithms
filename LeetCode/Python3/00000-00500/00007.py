class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        sign = 1 if x > 0 else -1
        limit_int = pow(2, 31) - 1 if sign == 1 else -pow(2, 31)
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        ans = sign * res
        if sign == 1:
            return ans if ans < limit_int else 0
        else:
            return ans if ans > limit_int else 0
