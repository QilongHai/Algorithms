class Solution:
    def convert(self, string: str, num_rows: int) -> str:
        if not string:
            return ''
        if num_rows == 1:
            return string
        res = ['' for _ in range(num_rows)]
        flag = -1
        index = 0
        for char in string:
            res[index] += char
            if index in [0, num_rows-1]:
                flag = -flag
            index += flag
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    string = 'LEETCODEISHIRING'
    num_rows = 3
    assert solution.convert(string, num_rows) == 'LCIRETOESIIGEDHN'
    print('ok')