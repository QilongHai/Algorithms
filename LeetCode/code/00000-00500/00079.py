from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ref: https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/
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


class SolutionTwo:
    # ref: https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < rows:
                return False
            if not 0 <= j < cols:
                return False
            if board[i][j] != word[k]:
                return False
            if k == word_len - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(i+1, j, k+1) or dfs(i, j-1, k +
                                          1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1)
            board[i][j] = tmp

            return res

        rows = len(board)
        cols = len(board[0])
        word_len = len(word)

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
