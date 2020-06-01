# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        pre = ListNode(-1)
        cur = pre
        while a and b:
            if a.val < b.val:
                val = a.val
                a = a.next
            else:
                val = b.val
                b = b.next
            cur.next = ListNode(val)
            cur = cur.next
        while a:
            cur.next = ListNode(a.val)
            cur = cur.next
            a = a.next
        while b:
            cur.next = ListNode(b.val)
            cur = cur.next
            b = b.next
        return pre.next
