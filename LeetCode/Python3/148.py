class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序--递归
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, head):
        if not head or not head.next:
            return head
        pre = head
        slow = head.next
        fast = head.next
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow

    def merge(self, left, right):
        res = ListNode(-1)
        pre = res
        while left and right:
            if left.val <= right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
            # 这一步是在消除left,right原链表的连接
            pre.next = None
        if left:
            pre.next = left
        if right:
            pre.next = right
        return res.next
