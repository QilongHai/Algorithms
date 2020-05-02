class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        while carry or i >= 0 or j >= 0:
            tmp = carry + (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0)
            carry = tmp // 10
            cur_val = tmp % 10
            res.append(str(cur_val))
            i -= 1
            j -= 1
        if carry > 0:
            res.append(str(carry))
        return ''.join(res[::-1])
