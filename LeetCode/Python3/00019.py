class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        slow = root
        fast = root
        while n > 0:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return root.next
