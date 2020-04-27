# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        tmp1 = ListNode(-1)
        tmp2 = ListNode(-1)
        p = tmp1
        q = tmp2
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next

        p.next = tmp2.next
        q.next = None

        return tmp1.next
