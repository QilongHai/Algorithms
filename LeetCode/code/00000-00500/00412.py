from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = [''] * n
        idx = 0
        for j in range(1, n + 1):
            tmp_3 = j % 3
            tmp_5 = j % 5
            if tmp_3 == 0 and tmp_5 == 0:
                res[idx] = 'FizzBuzz'
            elif tmp_3 == 0:
                res[idx] = 'Fizz'
            elif tmp_5 == 0:
                res[idx] = 'Buzz'
            else:
                res[idx] = str(j)
            idx += 1
        return res
