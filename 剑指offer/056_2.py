from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        data = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                data[i] += num & 1
                num >>= 1
        res = 0
        for j in range(32):
            res <<= 1
            res += data[31 - j] % 3
        if data[31] % 3 == 0:
            return res
        else:
            return ~(res ^ 0xffffffff)
