# ref: https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/

class Solution(object):
    def generateParenthesis(self, n):
        def dfs(cur_str, left, right):
            print([cur_str, left, right])
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        res = []
        cur_str = ''
        dfs(cur_str, n, n)
        return res


class SolutionTwo:
    def generateParenthesis(self, n):
        def dfs(cur_str, left, right):
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return
            if left < n:
                dfs(cur_str + '(', left + 1, right)
            if right < n:
                dfs(cur_str + ')', left, right + 1)

        cur_str = ''
        res = []
        dfs(cur_str, 0, 0)
        return res


if __name__ == '__main__':
    solution = SolutionTwo()
    ans = solution.generateParenthesis(2)
    print(ans)
