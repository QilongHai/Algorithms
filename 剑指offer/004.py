from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False

    def binary_search(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


class SolutionTwo:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

if __name__ == '__main__':
    solution = SolutionTwo()
    print(solution.findNumberIn2DArray(matrix, 5))