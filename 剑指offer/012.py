from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < rows:
                return False
            if not 0 <= j < cols:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '/'
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = tmp
            return res
            
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
        