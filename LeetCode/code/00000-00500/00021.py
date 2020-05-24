# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(-1)
        prev = pre_head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        return pre_head.next

    def mergeTwoLists_3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        if not l1 and not l2:
            return None
        pre = ListNode(-1)
        dummy = pre
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = ListNode(l1.val)
                l1 = l1.next if l1.next else None
            else:
                pre.next = ListNode(l2.val)
                l2 = l2.next if l2.next else None
            pre = pre.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return dummy.next
