from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        x = 0
        for i in nums:
            mask = mask ^ i
        diff = mask & (-mask)
        for j in nums:
            if diff & j:
                x ^= j
        return [x, mask ^ x]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    ans = s.singleNumber(nums)
    print(ans)
