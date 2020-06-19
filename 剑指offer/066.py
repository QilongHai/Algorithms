from typing import List


class Solution:
    def constructArr(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp_left = [1 for _ in range(n)]
        dp_right = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

        for i in range(1, n):
            dp_left[i] = dp_left[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            dp_right[j] = dp_right[j + 1] * nums[j + 1]
        for k in range(n):
            res[k] = dp_left[k] * dp_right[k]
        return res
