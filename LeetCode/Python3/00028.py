class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        for index in range(haystack_len):
            if haystack[index:index + needle_len] == needle:
                return index
        return -1
