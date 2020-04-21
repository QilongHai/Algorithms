from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0:
            return 0

        for j in range(1, col):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    case = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ans = 2
    solution = Solution()
    assert solution.uniquePathsWithObstacles(case) == ans, 'case: {} failed'.format(case)
    print('Test success')
