class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            if cache[i][j]:
                return cache[i][j]
            else:
                cache[i][j] = helper(i - 1, j) + helper(i, j - 1)
                return cache[i][j]

        cache = [[None for _ in range(n)] for _ in range(m)]
        return helper(m - 1, n - 1)


if __name__ == '__main__':
    case_list = [(7, 3, 28), (3, 2, 3)]
    solution = Solution()
    for item in case_list:
        ans = solution.uniquePaths(item[0], item[1])
        assert ans == item[2], 'case {} failed'.format(item)
    print('Test success!')