import copy
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

    def minPathSumTwo(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    case_a = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    case_b = copy.deepcopy(case_a)
    ans = 7
    solution = Solution()
    assert solution.minPathSum(case_a) == ans, 'case: {} failed in minPathSum method.'.format(case_a)
    print('Test minPathSum method success!')
    assert solution.minPathSumTwo(case_b) == ans, 'case: {} failed in minPathSumTwo method.'.format(case_b)
    print('Test minPathSumTwo method success!')
