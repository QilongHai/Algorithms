from typing import List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        def dfs(cur_str, next_digits):
            if len(next_digits) == 0:
                res.append(cur_str)
            else:
                for char in d[next_digits[0]]:
                    dfs(cur_str + char, next_digits[1:])

        res = []
        if digits:
            dfs('', digits)
        return res


class SolutionTwo:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        q = deque()
        q.append('')
        for item in digits:
            n = len(q)
            letters = d[item]
            for _ in range(n):
                tmp = q.popleft()
                for elem in letters:
                    q.append(tmp+elem)
        return list(q)




