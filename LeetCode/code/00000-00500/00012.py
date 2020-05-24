class Solution:
    def intToRoman(self, num: int) -> str:
        a = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']  # 个位
        b = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']  # 十位
        c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']  # 百位
        d = ['', 'M', 'MM', 'MMM']  # 千位

        return d[num // 1000] + c[(num // 100) % 10] + b[(num // 10) % 10] + a[num % 10]


if __name__ == '__main__':
    print('Start test...')
    num_list = [(3, 'III'), (4, 'IV'), (9, 'IX'), (58, 'LVIII'), (1994, 'MCMXCIV')]
    solution = Solution()
    for item in num_list:
        num = item[0]
        res = item[1]
        ans = solution.intToRoman(num)
        assert ans == res, 'case: {} fail. The return answer is {}'.format(item, ans)
    print('Test success!')
