class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseListIter(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre

    def reverseListRecursion(self, head: ListNode) -> ListNode:
        """
        我子节点下的所有节点都已经反转好了，现在就剩我和我的子节点 没有完成最后的反转了，所以反转一下我和我的子节点
        """
        if not head or not head.next:
            return head
        p = self.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    head = ListNode(1)
    dummy = head
    for i in range(2, 10):
        dummy.next = ListNode(i)
        dummy = dummy.next

    solution = Solution()
    tail = solution.reverseListIter(head)
    res = []
    while tail:
        res.append(tail.val)
        tail = tail.next
    print(res)
