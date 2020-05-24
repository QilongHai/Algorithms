class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return ''
        a = a.strip()
        b = b.strip()
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = []
        while carry or i >= 0 or j >= 0:
            tmp = carry + (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
            carry = tmp // 2
            cur_val = tmp % 2
            res.append(str(cur_val))
            i -= 1
            j -= 1
        if carry > 0:
            res.append(str(carry))
        return ''.join(res[::-1])
