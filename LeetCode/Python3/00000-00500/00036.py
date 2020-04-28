from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_valid = self.is_row_valid(board)
        col_valid = self.is_col_valid(board)
        square_valid = self.is_square_valid(board)
        return row_valid and col_valid and square_valid

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col_index in range(len(board[0])):
            tmp_cols = [row[col_index] for row in board]
            if not self.is_unit_valid(tmp_cols):
                return False
        return True

    def is_square_valid(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        tmp_set = set()
        tmp_list = []
        for i in unit:
            if i != '.':
                tmp_set.add(i)
                tmp_list.append(i)
        return len(tmp_set) == len(tmp_list)


if __name__ == '__main__':
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    ans = solution.isValidSudoku(board)
    assert ans == True, 'test fail'
    print('Test success')
