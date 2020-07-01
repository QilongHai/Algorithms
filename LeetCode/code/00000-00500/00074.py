from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start_row = 0
        end_row = m - 1
        start_col = n - 1
        end_col = 0
        while start_row <= end_row and start_col >= end_col:
            if matrix[start_row][start_col] == target:
                return True
            elif matrix[start_row][start_col] > target:
                start_col -= 1
            else:
                start_row += 1
        return False


class SolutionTwo:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
