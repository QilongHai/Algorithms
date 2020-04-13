class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        left_node = root
        right_node = root
        while n > 0:
            right_node = right_node.next
            n -= 1
        while right_node.next:
            right_node = right_node.next
            left_node = left_node.next

        left_node.next = left_node.next.next
        return root.next




