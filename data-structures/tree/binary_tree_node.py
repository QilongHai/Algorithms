class Node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

def count_nodes(bin_tree):
    if bin_tree is None:
        return 0
    else:
        return 1 + count_nodes(bin_tree.left) + count_nodes(bin_tree.right)

def pre_order(bin_tree):
    if bin_tree is None:
        return
    print(bin_tree.element)
    pre_order(bin_tree.left)
    pre_order(bin_tree.right)

def in_order(bin_tree):
    if bin_tree is None:
        return
    in_order(bin_tree.left)
    print(bin_tree.element)
    in_order(bin_tree.right)

def post_order(bin_tree):
    if bin_tree is None:
        return
    post_order(bin_tree.left)
    post_order(bin_tree.right)
    print(bin_tree.element)


class Empty(Exception):
    pass

class MyQueue:
    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._data.pop(0)
        self._size -= 1
        return answer

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

def level_order(bin_tree):
    q = MyQueue()
    q.enqueue(bin_tree)
    while not q.is_empty():
        x = q.dequeue()
        if x is None:
            continue
        print(x.data)
        q.enqueue(x.left)
        q.enqueue(x.right)

class MyStack:
    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        return self._size == 0
    def push(self, e):
        self._data.append(e)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self._data.pop()
        self._size -= 1
        return answer

def pre_order_iter(bin_tree):
    s = MyStack()
    while bin_tree is not None or s.is_empty():
        while bin_tree is not None:
            print(bin_tree.data)
            s.push(bin_tree.right)
            bin_tree = bin_tree.left
        bin_tree = s.pop()
