from typing import List


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

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for char in d[next_digits[0]]:
                    backtrack(combination + char, next_digits[1:])

        res = []
        if digits:
            backtrack('', digits)
        return res
