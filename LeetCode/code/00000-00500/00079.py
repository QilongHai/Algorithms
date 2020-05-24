from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, start_x, start_y, word_idx):
            if word_idx == len(word) - 1:
                return board[start_x][start_y] == word[word_idx]
            if board[start_x][start_y] == word[word_idx]:
                marked[start_x][start_y] = True
                for dir in dirs_list:
                    new_x = start_x + dir[0]
                    new_y = start_y + dir[1]
                    if (0 <= new_x < rows and 0 <= new_y < cols and not marked[new_x][new_y] and
                            dfs(board, new_x, new_y, word_idx + 1)):
                        return True
                marked[start_x][start_y] = False
            return False

        if not board:
            return False
        else:
            rows = len(board)
            cols = len(board[0])
            marked = [[False for _ in range(cols)] for _ in range(rows)]
            dirs_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for i in range(rows):
                for j in range(cols):
                    if dfs(board, i, j, 0):
                        return True
            return False

# ref: https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/
