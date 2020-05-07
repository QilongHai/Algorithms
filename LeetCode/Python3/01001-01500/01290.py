class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        res = 0
        base = 1
        while stack:
            res += stack.pop() * base
            base *= 2
        return res

    def getDecimalValue_2(self, head: ListNode) -> int:
        if not head:
            return 0
        ans = 0
        cur = head
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.val
        return ans


