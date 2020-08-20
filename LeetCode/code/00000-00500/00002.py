class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """"iter solution"""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(-1)
        cur = pre
        carry = 0
        while l1 or l2 or carry:
            tmp = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = tmp // 10
            cur_val = tmp % 10
            cur.next = ListNode(cur_val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return pre.next


class SolutionTwo:
    """"recursion solution"""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, 0)

    def helper(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if not l1 and not l2 and carry == 0:
            return None
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        node = ListNode(carry % 10)
        carry //= 10
        node.next = self.helper(l1, l2, carry)
        return node
