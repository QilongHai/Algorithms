class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_nnumbers(l1, l2):
    ret = ListNode(0)
    temp = ret
    carry = 0
    while l1 or l2 or carry:
        result = carry
        if l1:
            result += l1.val
            l1 = l1.next
        if l2:
            result += l2.val
            l2 = l2.next
        new_node = ListNode(result % 10)
        carry = result // 10
        temp.next = new_node
        temp = temp.next
    return ret.next

    pass