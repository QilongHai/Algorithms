class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        nums.sort()
        min_diff = float('inf')
        closet_sum = 0
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i + 1
            high = n - 1
            while low < high:
                tmp = nums[i] + nums[low] + nums[high]
                diff = tmp - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closet_sum = tmp
                if diff == 0:
                    return closet_sum
                elif diff < 0:
                    low += 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                else:
                    high -= 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
        return closet_sum
