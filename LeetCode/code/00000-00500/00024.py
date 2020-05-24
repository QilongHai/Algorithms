class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first

        return second

    def swapPairs_2(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head and head.next:
            p = head
            q = head.next
            pre.next = q
            p.next = q.next
            q.next = p
            pre = p
            head = p.next
        return dummy.next

