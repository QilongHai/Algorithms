class Solution:
    def findComplement(self, num: int) -> int:
        stack = []
        while num:
            stack.append(num % 2)
            num >>= 1
        stack = stack[::-1]
        for i in range(len(stack)):
            if stack[i] == 0:
                stack[i] = 1
            elif stack[i] == 1:
                stack[i] = 0
        res = 0
        for j in stack:
            res = res * 2 + j
        return res
