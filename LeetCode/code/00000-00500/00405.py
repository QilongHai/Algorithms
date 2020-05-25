class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        d = dict()
        for i in range(10):
            d[i] = str(i)
        j = 10
        for char in ['a', 'b', 'c', 'd', 'e', 'f']:
            d[j] = char
            j += 1
        if num < 0:
            num = num & 0xffffffff
        res = []
        while num:
            res.append(d[num % 16])
            num //= 16
        return ''.join(res[::-1])


class SolutionTwo:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        d = '0123456789abcdef'
        if num < 0:
            num = num & 0xffffffff
        res = ''
        mask = 0b1111
        while num:
            res += d[num & mask]
            num >>= 4
        return res[::-1]
    # 使用 & 操作符，把负数前置无限个 1 和 正数 0xFFFFFFFF 前置无限个 0 与运算，那么负数前置的 1 全部被干掉成为 0,
    # 即成为正数，是 python 中获取 【x 位整型】补码形式的一种操作
