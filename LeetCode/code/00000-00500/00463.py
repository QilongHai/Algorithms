from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res


class SolutionTwo:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= rows:
                return 1
            if j < 0 or j >= cols:
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
