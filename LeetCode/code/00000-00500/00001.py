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


class SolutionTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], idx]
            d[num] = idx


if __name__ == '__main__':
    s = SolutionTwo()
    ans = s.twoSum([2, 7, 11, 15], 9)
    print(ans)
