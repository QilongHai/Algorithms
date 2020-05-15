from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_list = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                cnt_list[i] += num & 1
                num >>= 1
        for j in range(32):
            cnt_list[j] = cnt_list[j] % 3
        res = 0
        for k in cnt_list[::-1]:
            res = res * 2 + k
        if cnt_list[31] % 3:
            res = ~(res ^ 0xffffffff)
        return res


class SolutionTwo:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, -3, 2]
    ans = s.singleNumber(nums)
    print(ans)