class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup_set = set()
        max_len = 0
        cur_len = 0
        for idx in range(len(s)):
            cur_len += 1
            while s[idx] in lookup_set:
                lookup_set.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup_set.add(s[idx])
        return max_len
