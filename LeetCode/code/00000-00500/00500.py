from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = dict()
        up = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        mid = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        low = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        for i in up:
            d[i] = 'up'
            d[i.lower()] = 'up'
        for j in mid:
            d[j] = 'mid'
            d[j.lower()] = 'mid'
        for k in low:
            d[k] = 'low'
            d[k.lower()] = 'low'
        res = []
        for word in words:
            ans = set()
            for s in word:
                ans.add(d[s])
            if len(ans) == 1:
                res.append(word)
        return res
