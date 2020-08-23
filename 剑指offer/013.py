from collections import deque


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1
        queue = deque()
        queue.append((0, 0))
        res = 0
        while queue:
            tmp = queue.popleft()
            res += 1
            x, y = tmp[0], tmp[1]
            for i, j in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                new_x = x + i
                new_y = y + j
                if not 0 <= new_x < m:
                    continue
                if not 0 <= new_y < n:
                    continue
                if self.add_digit(new_x, new_y) > k:
                    continue
                if matrix[new_x][new_y] == 1:
                    continue
                matrix[new_x][new_y] = 1
                queue.append((new_x, new_y))
        return res

    def add_digit(self, x, y):
        res = 0
        while x:
            res += x % 10
            x //= 10
        while y:
            res += y % 10
            y //= 10
        return res


class SolutionTwo:

    def __init__(self):
        self.count = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        def is_valid(x, y):
            res = 0
            for i in [x, y]:
                while i:
                    res += i % 10
                    i //= 10
            return True if res <= k else False

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if not is_valid(i, j):
                return False
            if board[i][j] == 1:
                return False
            board[i][j] = 1
            self.count += 1
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)

        board = [[0 for _ in range(n)] for _ in range(m)]
        dfs(0, 0)
        return self.count
