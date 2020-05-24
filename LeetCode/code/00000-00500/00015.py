from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = n - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1
        return res


if __name__ == "__main__":
    case = [-1, 0, 1, 2, -1, -4]
    res = [[-1, 0, 1], [-1, -1, 2]]
    solution = Solution()
    ans = solution.threeSum(case)
    for i in ans:
        if i in res:
            pass
        else:
            assert i in res == i in ans, 'case miss match. res: {}, ans: {}'.format(res, ans)
    assert len(ans) == len(res), 'test case match'
    print('Test success')
