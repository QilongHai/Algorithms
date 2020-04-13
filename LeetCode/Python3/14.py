from typing import List


class Solution:
    def longestCommonPrefix(self, str_list: List[str]) -> str:
        if not str_list:
            return ''
        if len(str_list) == 0:
            return ''
        s = str_list[0]
        for i in range(1, len(str_list)):
            while str_list[i].find(s) != 0:
                s = s[:-1]
        return s

a = ["flower","flow","flight"]
s = Solution()
res = s.longestCommonPrefix(a)
print(res)