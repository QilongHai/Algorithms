from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        stack = []
        while K:
            stack.append(K % 10)
            K //= 10

        carry = 0
        i = len(A) - 1
        j = len(stack) - 1
        new_stack = stack[::-1]
        res = []
        while carry or i >= 0 or j >= 0:
            tmp = carry + (A[i] if i >= 0 else 0) + (new_stack[j] if j >= 0 else 0)
            res.append(tmp % 10)
            carry = tmp // 10
            i -= 1
            j -= 1
        if carry > 0:
            res.append(carry)
        return res[::-1]
