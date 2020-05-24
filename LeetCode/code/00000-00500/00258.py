class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            stack = []
            while num:
                stack.append(num % 10)
                num //= 10
            res = sum(stack)
            if 0 <= res <= 9:
                return res
            else:
                num = res
