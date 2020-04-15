class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True

        stack = []
        while x:
            stack.append(x % 10)
            x //= 10
        return True if stack == stack[::-1] else False
