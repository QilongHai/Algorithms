from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        res = []
        for i in set(A[0]):
            min_count = min([j.count(i) for j in A])
            res += [i for _ in range(min_count)]
        return res
