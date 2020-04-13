from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            matrix[i].reverse()
    def rotate_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = matrix[::-1]
        # print(matrix)
        for i in range(0, n):
            for j in range(i+1, n):
                print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
a = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]
c = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
s.rotate_2(matrix)
# print(matrix)
