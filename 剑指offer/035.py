class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        d = dict()
        node = head
        # 创建所有节点
        while node:
            d[node] = Node(node.val, None, None)
            node = node.next

        node = head
        # 节点连接
        while node:
            d[node].next = d.get(node.next)
            d[node].random = d.get(node.random)
            node = node.next
        return d[head]
