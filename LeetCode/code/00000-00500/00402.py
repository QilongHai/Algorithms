class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            if not stack:
                stack.append(digit)
            else:
                if k and stack and stack[-1] > digit:
                    stack.pop()
                    k -= 1
                stack.append(digit)

        ans = stack[:-k] if k > 0 else stack
        res = ''.join(ans).lstrip('0')
        if res == '':
            res = '0'
        return res
