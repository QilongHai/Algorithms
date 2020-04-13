from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, val in enumerate(nums):
            d[val] = idx
        for i, num in enumerate(nums):
            j = d.get(target - num)
            if j != i and j is not None:
                return [i, j]


s = Solution()
ans = s.twoSum([2, 7, 11, 15], 9)
print(ans)
