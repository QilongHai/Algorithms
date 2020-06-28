class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        if n == 2:
            return []
        if n == 3:
            return []
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def is_valid(board, row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            r_row = row
            r_col = col
            while r_row > 0 and r_col < n - 1:
                r_row -= 1
                r_col += 1
                if board[r_row][r_col] == 'Q':
                    return False
            l_row = row
            l_col = col
            while l_row > 0 and l_col > 0:
                l_row -= 1
                l_col -= 1
                if board[l_row][l_col] == 'Q':
                    return False
            return True

        def dfs(board, start_row, res):
            if start_row == n:
                ans = ['' * n for _ in range(n)]
                for idx, row in enumerate(board):
                    ans[idx] = ''.join(row)
                res.append(ans)
                return
            for col in range(n):
                if not is_valid(board, start_row, col):
                    continue
                board[start_row][col] = 'Q'
                dfs(board, start_row+1, res)
                board[start_row][col] = '.'

        dfs(board, 0, res)
        return res