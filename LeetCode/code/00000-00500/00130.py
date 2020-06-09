from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] in ['X', '#']:
                return
            board[i][j] = '#'
            dfs(board, i-1, j)
            dfs(board, i+1, j)
            dfs(board, i, j-1)
            dfs(board, i, j+1)

        if not board or len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                is_edge = (i in [0, m - 1] or j in [0, n - 1])
                if is_edge and board[i][j] == 'O':
                    dfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
