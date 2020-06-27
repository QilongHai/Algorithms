from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.merge_two_list(l1, l2)

    def merge_two_list(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        pre = ListNode(-1)
        cur = pre
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return pre.next
