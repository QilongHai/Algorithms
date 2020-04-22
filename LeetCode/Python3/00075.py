import copy
from typing import List


class Solution:
    def sortColorsNaive(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for val in nums:
            if val == 0:
                red += 1
            elif val == 1:
                white += 1
            else:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for j in range(red, white + red):
            nums[j] = 1
        for k in range(len(nums) - white, len(nums)):
            nums[k] = 2
        # return nums

    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        if size < 2:
            return
        zero = 0
        two = size
        i = 0
        while i < two:
            if nums[i] == 0:
                self.swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                self.swap(nums, i, two)


if __name__ == '__main__':
    solution = Solution()
    case_a = [2, 0, 2, 1, 1, 0]
    case_b = copy.deepcopy(case_a)
    ans = [0, 0, 1, 1, 2, 2]

    solution.sortColorsNaive(case_a)
    assert case_a == ans, 'case: {} failed'.format(case_a)

    solution.sortColors(case_b)
    assert case_b == ans, 'case: {} failed'.format(case_b)

    print('Test success!')
