class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''
        i = len(num1) - 1
        j = len(num2) - 1
        k = max(len(num1), len(num2)) + 1
        carry = 0
        res = ['' for _ in range(k)]
        k -= 1
        while carry or i >= 0 or j >= 0:
            tmp = carry + (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0)
            carry = tmp // 10
            res[k] = str(tmp % 10)
            i -= 1
            j -= 1
            k -= 1
        return ''.join(res).strip()
