class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if not s:
            return ''
        if num_rows == 1:
            return s
        res = [''] * num_rows
        cur_row = 0
        down = -1
        for char in s:
            res[cur_row] += char
            if cur_row == 0 or cur_row == num_rows - 1:
                down = -down
            cur_row += down
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    string = 'LEETCODEISHIRING'
    num_rows = 3
    assert solution.convert(string, num_rows) == 'LCIRETOESIIGEDHN'
    print('ok')
