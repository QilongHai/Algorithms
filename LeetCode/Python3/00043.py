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
