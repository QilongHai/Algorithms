class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        product = [0 for _ in range((len(num1) + len(num2)))]
        pos = len(product) - 1

        for i in reversed(num1):
            temp = pos
            for j in reversed(num2):
                product[temp] += int(i) * int(j)
                product[temp - 1] += product[temp] // 10
                product[temp] %= 10
                temp -= 1
            pos -= 1

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))


class SolutionTwo:
    def multiply(self, num1: str, num2: str) -> str:
        """ref: https://www.cnblogs.com/grandyang/p/4395356.html"""
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                tmp = mul + res[p2]
                res[p1] += tmp // 10
                res[p2] = tmp % 10
        return ''.join(res).lstrip('0')
