# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        k = k % n
        if k == 0:
            return head
        pre = head
        post = head
        for i in range(k):
            post = post.next
        while post.next:
            pre = pre.next
            post = post.next
        tmp = pre.next
        pre.next = None
        post.next = head

        return tmp
