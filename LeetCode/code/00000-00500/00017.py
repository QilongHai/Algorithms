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


class SolutionThree:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
             '8': 'tuv', '9': 'wxyz'}
        k = len(digits)
        if k == 1:
            return list(d[digits])
        res = []

        def dfs(start_idx, path):
            if start_idx == k:
                res.append(''.join(path))
                return
            for char in d[digits[start_idx]]:
                path.append(char)
                dfs(start_idx+1, path)
                path.pop()

        dfs(0, [])
        return res
