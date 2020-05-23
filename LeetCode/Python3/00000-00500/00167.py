from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for idx, val in enumerate(numbers):
            d[val] = idx + 1
        for idx, num in enumerate(numbers):
            if target - num in d and d.get(target - num) != idx + 1:
                return [min(idx + 1, d.get(target - num)), max(idx + 1, d.get(target - num))]
