class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        res = [[None for _ in range(n)] for _ in range(n)]
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        num = 1
        while col_start <= col_end and row_start <= row_end:
            for idx in range(col_start, col_end + 1):
                res[row_start][idx] = num
                num += 1
            row_start += 1

            for row in range(row_start, row_end + 1):
                res[row][col_end] = num
                num += 1
            col_end -= 1

            for idx in range(col_end, col_start - 1, -1):
                res[row_end][idx] = num
                num += 1
            row_end -= 1

            for idx in range(row_end, row_start - 1, -1):
                res[idx][col_start] = num
                num += 1
            col_start += 1

        return res
