class Empty(Exception):
    pass

class LinkedQueue:
    #  -----------------------------write a class of private Node-----------------------------
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #  ------------------------------start queue method------------------------------------------

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._head._element

    def enqueue(self, e):
        new = self._Node(e, None)  # create a tail node, so set next is None
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

