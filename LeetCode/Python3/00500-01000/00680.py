class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return is_valid(low + 1, high) or is_valid(low, high - 1)
        return True