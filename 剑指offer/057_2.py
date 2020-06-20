from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for n in range(2, target + 1):
            tmp = target - n * (n - 1) // 2
            if tmp <= 0:
                break
            if not tmp % n:
                a = tmp // n
                res.append([a + i for i in range(n)])
        return res[::-1]
