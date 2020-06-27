class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        jump = dummy
        dummy.next = head
        left = head
        right = head

        while True:
            count = 0
            while count < k and right:
                right = right.next
                count += 1
            if count == k:
                pre = right
                cur = left
                for _ in range(k):
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                jump.next = pre
                jump = left
                left = right
            else:
                return dummy.next


class SolutionTwo:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while tmp and count:
                count -= 1
                stack.append(tmp)
                tmp = tmp.next
            if count > 0:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            head = tmp
        return dummy.next



