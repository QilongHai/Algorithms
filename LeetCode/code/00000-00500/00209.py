from typing import List
import bisect


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        # 总和都小于 s 时候
        if nums[-1] < s:
            return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res


class SolutionTwo:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = float('inf')
        tmp = 0
        for j in range(n):
            tmp += nums[j]
            while tmp >= s:
                res = min(res, j-i+1)
                tmp -= nums[i]
                i += 1
        return res if res != float('inf') else 0
