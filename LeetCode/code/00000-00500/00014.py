from typing import List

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


class SolutionTwo:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0:
                s = s[0:-1:1]
        return s


class SolutionThree:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs)
        if n < 2:
            return strs[0]
        res = strs[0]
        for i in range(1, n):
            if len(res) == 0 or len(strs[i]) == 0:
                return ''
            else:
                min_len = min(len(res), len(strs[i]))
                tmp = ''
                for j in range(min_len):
                    if res[j] == strs[i][j]:
                        tmp += res[j]
                    else:
                        break
                res = tmp
        return res

