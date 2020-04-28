class SolutionOne:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = []
        for i in zip(*strs):
            if len(set(i)) == 1:
                res.append(i[0])
            else:
                break
        return ''.join(res)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0:
                s = s[0:-1:1]
        return s
