from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = one_word * len(words)
        n = len(s)
        word_count = Counter(words)
        res = []
        for i in range(n-all_len+1):
            tmp = s[i:i+all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == word_count:
                res.append(i)
        return res
        