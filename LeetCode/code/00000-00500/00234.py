# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # list
    def isPalindrome_1(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i = 0
        j = len(arr) - 1
        while i <= j:
            if arr[i] == arr[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    # reverse linklist
    def isPalindrome_2(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        a = head
        b = self.reverse_linklist(slow)
        res = True
        while res and a and b:
            if a.val != b.val:
                res = False
            a = a.next
            b = b.next
        return res

    @staticmethod
    def reverse_linklist(head):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
