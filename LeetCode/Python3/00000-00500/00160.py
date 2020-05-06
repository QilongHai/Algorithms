# 我先走我的路，再走你的路，你先走你的路，再走我的路，这样咱俩走的路程就一样了，速度一样，
# 那么肯定在咱俩两条路的交叉口相遇，并一起走向终点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a
