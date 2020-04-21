class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = a.strip()
        b = b.strip()
        i = len(a) - 1
        j = len(b) - 1
        stack = []
        while carry or i >= 0 or j >= 0:
            tmp = carry + (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
            cur_val = tmp % 2
            carry = tmp // 2
            stack.append(str(cur_val))
            i -= 1
            j -= 1

        return ''.join(stack[::-1])
