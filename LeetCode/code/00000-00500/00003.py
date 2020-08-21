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


class SolutionTwo:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_set = set()
        n = len(s)
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in tmp_set:
                tmp_set.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                tmp_set.remove(s[i])
                i += 1
        return ans


class SolutionThree:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start, end = 0, 0
        length = 0
        res = 0
        seen = dict()
        while end < n:
            cur_str = s[end]
            if cur_str in seen and seen[cur_str] >= start:
                start = seen[cur_str] + 1
                length = end - start
            seen[cur_str] = end
            end += 1
            length += 1
            if length > res:
                res = length
        return res




if __name__ == '__main__':
    input_list = ["abcabcbb", "bbbbb", "pwwkew"]
    solution_obj = SolutionTwo()
    for item in input_list:
        print(solution_obj.lengthOfLongestSubstring(item))
