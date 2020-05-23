class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while True:
            stack = []
            while n:
                stack.append(n % 10)
                n //= 10
            res = 0
            for i in stack:
                res += i ** 2
            if res == 1:
                return True
            else:
                n = res
                count += 1
                if count == 1000:
                    return False
                continue
