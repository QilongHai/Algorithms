from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row_num in range(numRows):
            row = [0 for _ in range(row_num + 1)]
            row[0] = 1
            row[-1] = 1
            for j in range(1, len(row) - 1):
                row[j] = res[row_num - 1][j - 1] + res[row_num - 1][j]
            res.append(row)

        return res


class SolutionTwo:
    """
    ref: https://leetcode-cn.com/problems/pascals-triangle/solution/qu-qiao-jie-fa-cuo-yi-wei-zai-zhu-ge-xiang-jia-28m/
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            row = [x + y for x, y in zip([0] + res[-1], res[-1] + [0])]
            res.append(row)
        return res
