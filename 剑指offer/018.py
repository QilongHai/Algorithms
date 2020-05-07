# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
            pre = pre.next
            cur = cur.next
        return head
