class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return False
        if n == 1:
            return True
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count == 1
