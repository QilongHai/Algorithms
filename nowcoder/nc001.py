#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s, t):
        # write code here
        res = []
        carry = 0
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0 or carry:
            val = (int(s[i]) if i >= 0 else 0) + (int(t[j]) if j >= 0 else 0) + carry
            res.append(str(val % 10))
            carry = val // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])
