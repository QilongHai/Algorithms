class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]

        return res + d[s[-1]]


if __name__ == '__main__':
    case_list = [('III', 3), ('IV', 4), ('IX', 9), ('LVIII', 58), ('MCMXCIV', 1994)]
    solution = Solution()
    for item in case_list:
        roman_str = item[0]
        res = item[1]
        ans = solution.romanToInt(roman_str)
        assert ans == res, 'case {} fail. The ans is {}.'.format(item, ans)
    print('Test success!')
