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


class SolutionTwo:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        pre = ListNode(-1)
        cur = pre
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return pre.next
