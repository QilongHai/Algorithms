from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(idx):
            if idx == len(char_list) - 1:
                res.append(''.join(char_list))
                return
            d = dict()
            for i in range(idx, len(char_list)):
                if char_list[i] in d:
                    continue
                d[char_list[i]] = 1
                char_list[i], char_list[idx] = char_list[idx], char_list[i]
                dfs(idx+1)
                char_list[i], char_list[idx] = char_list[idx], char_list[i]

        if not s:
            return []
        res = []
        char_list = list(s)
        dfs(0)
        return res