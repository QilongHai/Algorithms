from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res = res ^ i
        return res
"""
任何数和0做异或运算，结果仍然是原来的数
任何数和其自身做异或运算
异或运算满足交换律和结合律
"""