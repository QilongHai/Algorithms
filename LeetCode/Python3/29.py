class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        a = abs(dividend)
        b = abs(divisor)
        if dividend == 0:
            return 0
        if b == 1:
            return min(max(-2 ** 31, sign * a), 2 ** 31 - 1)

        while a >= b:
            temp = b
            count = 1
            while temp << 1 <= a:
                print(a, b, temp, count)
                temp <<= 1
                count <<= 1
            a -= temp
            res += count
        res = sign * res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


s = Solution()
a = 10000000
b = 3
print(s.divide(a, b))
