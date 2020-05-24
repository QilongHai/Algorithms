from typing import List


class Solution:

    # Time Out
    def wiggleMaxLength_(self, nums: List[int]) -> int:
        def dfs(nums, index, is_up):
            max_count = 0
            for i in range(index + 1, n):
                if (is_up and nums[i] > nums[index]) or (not is_up and nums[i] < nums[index]):
                    flag = not is_up
                    max_count = max(max_count, 1 + dfs(nums, i, flag))
            return max_count

        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return n
        return 1 + max(dfs(nums, 0, True), dfs(nums, 0, False))

    # dp
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)

    # greedy
    def wiggleMaxLength__(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return n
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        return count
