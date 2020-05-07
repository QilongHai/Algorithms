# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        a = dummy
        for _ in range(m - 1):
            a = a.next
        pre = None
        cur = a.next
        for _ in range(n - m + 1):
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        a.next.next = cur
        a.next = pre
        return dummy.next
