from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(cur_i, cur_j):
            if not 0 <= cur_i < len(grid):
                return 0
            if not 0 <= cur_j < len(grid[0]):
                return 0
            if grid[cur_i][cur_j] != 1:
                return 0
            grid[cur_i][cur_j] = 0
            res = 1
            for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_i = cur_i + i
                new_j = cur_j + j
                res += dfs(new_i, new_j)
            return res

        res = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                res = max(dfs(i, j), res)
        return res


class SolutionTwo:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                cur = 0
                q = deque()
                q.append([i, j])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_i >= len(grid):
                        continue
                    if cur_j < 0 or cur_j >= len(grid[0]):
                        continue
                    if grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        new_i = x + cur_i
                        new_j = y + cur_j
                        q.append([new_i, new_j])
                res = max(cur, res)
        return res


class SolutionThree:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(i, j):
            if i < 0 or i >= rows:
                return 0
            if j < 0 or j >= cols:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return 1 + area(i-1, j) + area(i+1, j) + area(i, j-1) + area(i, j+1)

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cur_area = area(i, j)
                    res = max(res, cur_area)
        return res